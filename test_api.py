import requests
import numpy as np

# URL of your running FastAPI server
url = "http://127.0.0.1:8000/predict"

# Generate one random row of test data
data = {
    "urgent_score": int(np.random.randint(1, 6)),
    "impact_score": int(np.random.randint(1, 6)),
    "delay_hours": int(np.random.randint(0, 48)),
    "affected_users": int(np.random.randint(1, 1000)),
    "critical_flag": int(np.random.randint(0, 2))
}

print("Sending data:", data)

# Send POST request
try:
    response = requests.post(url, json=data)
    print("Status code:", response.status_code)
    
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Server response was:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
