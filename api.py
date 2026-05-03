import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("hypoxia_model.pkl")
features = joblib.load("features.pkl")

app = FastAPI(title="Pilot Hypoxia Detection API")

class VitalSigns(BaseModel):
    HR: float
    RESP: float
    spo2_rolling: float
    hr_rolling: float
    spo2_drop: float
    hr_change: float

@app.get("/")
def home():
    return {"message": "Pilot Hypoxia Detection API is running"}

@app.post("/predict")
def predict(data: VitalSigns):
    input_df = pd.DataFrame([data.model_dump()])
    input_df = input_df[features]

    risk_probability = model.predict_proba(input_df)[0][1]
    risk_label = int(risk_probability > 0.1)

    return {
        "risk_probability": round(float(risk_probability), 3),
        "risk_label": risk_label,
        "interpretation": "HIGH RISK" if risk_label == 1 else "LOW RISK"
    }