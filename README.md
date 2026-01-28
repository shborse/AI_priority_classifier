# AI Priority Classifier

A **FastAPI-based machine learning service** that classifies incoming requests by priority level using a trained scikit-learn model.
The project demonstrates end-to-end ML integration, API design, and local deployment readiness.



## Overview

This repository contains a complete backend service for priority classification, along with a lightweight frontend interface for interaction.

**Key capabilities**

* Priority prediction using a pre-trained ML model
* RESTful API built with FastAPI
* Interactive API documentation (Swagger UI)
* Static frontend for user input and response visualization



## Project Structure


AI_priority_classifier/
│
├── app.py                  # FastAPI application entry point
├── priority_model.pkl      # Serialized ML model
├── frontend/               # Static frontend assets
│   ├── index.html
│   ├── script.js
│   └── style.css
├── test_api.py             # API testing script
├── README.md


## Execution Model

> This project is intended to be **run locally or deployed on a server**.
> GitHub does not execute backend services or machine learning models.

To use the application, the repository must be cloned and executed in a local or cloud environment.


## Local Setup Instructions

### Prerequisites

* Python 3.10
* Conda (recommended)


### 1. Clone the repository

bash
git clone https://github.com/shborse/AI_priority_classifier.git
cd AI_priority_classifier


### 2. Create and activate a Conda environment

bash
conda create -n priority_env python=3.10
conda activate priority_env


### 3. Install dependencies

bash
conda install -y pandas numpy scikit-learn scipy
pip install fastapi uvicorn joblib


### 4. Start the application

bash
uvicorn app:app --reload
The backend will be available at:
http://127.0.0.1:8000


## Accessing the Application

* **API Documentation (Swagger UI)**
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **Frontend Interface**
  [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Example

**Request**

json
POST /predict
{
  "text": "Urgent server outage"
}


**Response**

json
{
  "priority": "High"
}

## Frontend

The frontend is implemented using **HTML, CSS, and JavaScript** and communicates with the backend through HTTP requests.
It is intended for demonstration and testing purposes.

## Technology Stack

* **Backend:** FastAPI (Python)
* **Machine Learning:** scikit-learn, joblib
* **Frontend:** HTML, CSS, JavaScript
* **Environment Management:** Conda

## Future Enhancements

* Add `requirements.txt` for simplified setup
* Containerize using Docker
* Deploy backend to cloud platforms (Render / Railway)
* Host frontend using GitHub Pages or Netlify
* Extend model and dataset

## Author

**Shreya Borse**
Engineering Student | Backend & Machine Learning
GitHub: [https://github.com/shborse](https://github.com/shborse)
