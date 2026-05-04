import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("hypoxia_model.pkl")

app = FastAPI(title="Hypoxia Detection API")

class VitalSigns(BaseModel):
    resp_mean: float
    resp_std: float
    resp_min: float
    resp_max: float
    pulse_mean: float
    pulse_std: float
    hr_mean: float
    hr_std: float

@app.get("/")
def home():
    return {"message": "Hypoxia Detection API is running"}

@app.post("/predict")
def predict(data: VitalSigns):
    values = np.array([[
        data.resp_mean,
        data.resp_std,
        data.resp_min,
        data.resp_max,
        data.pulse_mean,
        data.pulse_std,
        data.hr_mean,
        data.hr_std
    ]])

    pred = model.predict(values)[0]
    proba = model.predict_proba(values)[0]

    if 1 in model.classes_:
        idx = list(model.classes_).index(1)
        prob = proba[idx]
    else:
        prob = 0.0

    return {
        "prediction": int(pred),
        "probability": round(float(prob), 3),
        "interpretation": "HYPOXIA" if int(pred) == 1 else "NORMAL"
    }