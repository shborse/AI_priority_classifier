from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# --------------------------------------------------
# App
# --------------------------------------------------
app = FastAPI(title="Priority Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Load model safely
# --------------------------------------------------
model = joblib.load("priority_model.pkl")


#try:
    #if os.path.exists(MODEL_PATH):
     #   model = joblib.load(MODEL_PATH)
      #  print("✅ Model loaded successfully")
    #else:
     #   raise FileNotFoundError(f"{MODEL_PATH} not found")
#except Exception as e:
 #   print(f"⚠️ Failed to load model: {e}")
  #  print("⚠️ Backend will still start, but /predict will not work until the model is fixed!")
   # model = None  # mark as None for safety

# --------------------------------------------------
# Input schema
# --------------------------------------------------
class PriorityInput(BaseModel):
    urgent_score: int
    impact_score: int
    affected_users: int
    delay_hours: int
    critical_flag: int

# --------------------------------------------------
# Health check
# --------------------------------------------------
@app.get("/")
def home():
    return {"status": "Priority API running 🚀"}

# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------
@app.post("/predict")
def predict_priority(data: PriorityInput):
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded. Check priority_model.pkl"
        )

    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Enforce exact feature order from training
        input_df = input_df[model.feature_names_in_]

        # Predict class
        pred_class = int(model.predict(input_df)[0])
        probs = model.predict_proba(input_df)[0]
        confidence = float(probs[pred_class])

        # Map decision
        if confidence < 0.6:
            decision = "Needs human review"
        elif pred_class == 2:
            decision = "High Priority"
        elif pred_class == 1:
            decision = "Medium Priority"
        else:
            decision = "Low Priority"

        return {
            "priority_class": pred_class,
            "decision": decision,
            "confidence": round(confidence, 3)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
