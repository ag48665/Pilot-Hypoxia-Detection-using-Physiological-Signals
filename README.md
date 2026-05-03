# 🧠 Pilot Hypoxia Detection using Physiological Signals

## 📌 Overview

This project develops a machine learning model to detect hypoxia risk in pilots based on physiological signals such as oxygen saturation (SpO₂), heart rate, and respiration.

The goal is to build a safety-oriented system that prioritizes early detection of oxygen deprivation.

---

## 📊 Data

* Physiological signals dataset (SpO₂, HR, RESP)
* Time-series measurements
* Preprocessed to remove missing values and normalize column names

---

## ⚙️ Feature Engineering

Engineered temporal features to capture physiological dynamics:

* Rolling averages (SpO₂, HR)
* Signal changes (ΔSpO₂, ΔHR)

These features allow the model to detect trends rather than single measurements.

---

## 🤖 Model

* Algorithm: Random Forest Classifier
* Features:

  * HR
  * RESP
  * SpO₂ rolling average
  * HR rolling average
  * SpO₂ change
  * HR change

---

## 📈 Results

### Default threshold (0.5)

* Recall (risk): ~0.78
* Precision: ~0.70

### Optimized threshold (0.1)

* Recall (risk): **1.00**
* Precision: ~0.50

👉 Prioritized recall to avoid missing hypoxia events in a safety-critical scenario.

---

## 🧠 Key Insights

* SpO₂ trends (rolling average) are the strongest predictor of hypoxia risk
* Respiratory rate significantly contributes to detection
* Single-point measurements are less informative than temporal patterns

---

## 🚀 Future Improvements

* Integrate NASA flight crew datasets
* Real-time monitoring system (API)
* Visualization dashboard

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn

---
## 🌐 API

The model is exposed via a FastAPI service.

### Run locally:

```bash
uvicorn api:app --reload
```

### Endpoint:

POST /predict

### Example request:

```json
{
  "HR": 94,
  "RESP": 26,
  "spo2_rolling": 97,
  "hr_rolling": 93.6,
  "spo2_drop": 0,
  "hr_change": 0
}
```

### Example response:

```json
{
  "risk_probability": 0.0,
  "risk_label": 0,
  "interpretation": "LOW RISK"
}
```


## 📌 Author

Bioinformatics & Data Science student focusing on ML in healthcare and aviation

Agata Gabara
