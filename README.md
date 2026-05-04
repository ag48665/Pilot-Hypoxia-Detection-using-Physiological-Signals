# 🧠 Pilot Hypoxia Detection using Physiological Signals

## 📌 Overview

This project presents a machine learning system for detecting hypoxia risk based on physiological signals such as respiration, pulse, heart rate, and oxygen saturation.

The goal is to support safety-critical environments (e.g., aviation) by enabling early detection of oxygen deprivation patterns.

---

## 📊 Data

The model is trained on physiological signals from the BIDMC dataset:

* SpO₂ (oxygen saturation)
* Heart rate (HR)
* Respiration (RESP)
* Pulse

The data consists of time-series recordings collected from clinical monitoring systems.

The dataset was processed into fixed-size windows to extract statistical features.

---

## ⚙️ Feature Engineering

Statistical features were extracted from physiological signals using fixed-size time windows:

**Respiration:**

* mean
* standard deviation
* minimum
* maximum

**Pulse:**

* mean
* standard deviation

**Heart Rate:**

* mean
* standard deviation

These features capture variability and distribution patterns in physiological signals rather than relying on single-point measurements.

---

## 🤖 Model

* Algorithm: Random Forest Classifier

**Features:**

* resp_mean
* resp_std
* resp_min
* resp_max
* pulse_mean
* pulse_std
* hr_mean
* hr_std

The model predicts the probability of hypoxia based on physiological signal patterns.

---

## 📈 Results

* Accuracy: ~0.95

The model demonstrates strong performance in distinguishing normal vs hypoxia conditions based on statistical signal features.

---

## 🧠 Key Insights

* Variability in respiration is a strong indicator of physiological state
* Pulse and heart rate patterns contribute significantly to prediction
* Aggregated statistical features outperform raw signal values

---

## 🚀 Future Improvements

* Integration of additional publicly available physiological datasets
* Real-time monitoring system for continuous signal analysis
* Visualization dashboard for physiological trends
* Explainable AI techniques (e.g., SHAP) for model interpretability
* Deployment as a scalable web service

---

## 🛠️ Tech Stack

* Python
* NumPy
* Scikit-learn
* FastAPI
* Uvicorn
* WFDB

---

## 🌐 API

The model is exposed via a FastAPI service.

---

## 🌍 Live Demo

Run the API locally and open interactive docs:

👉 http://127.0.0.1:8001/docs

> Note: This works only when the server is running locally.

---
## 💡 Live Example

Example prediction from deployed API:

```json
{
  "prediction": 0,
  "probability": 0.17,
  "interpretation": "NORMAL"
}

---

### ▶ Run locally

```bash
python -m uvicorn api:app --host 127.0.0.1 --port 8001
```

---

### 📍 Endpoint

**POST** `/predict`

---

### 🧪 Example request

```json
{
  "resp_mean": 18,
  "resp_std": 2,
  "resp_min": 14,
  "resp_max": 22,
  "pulse_mean": 75,
  "pulse_std": 5,
  "hr_mean": 78,
  "hr_std": 6
}
```

---

### 📤 Example response

```json
{
  "prediction": 0,
  "probability": 0.17,
  "interpretation": "NORMAL"
}
```

---

## 🌍 Live Demo

You can test the model via interactive API docs:

👉 https://pilot-hypoxia-detection-using.onrender.com/docs

---


## ⚙️ System Architecture

1. Raw physiological signals are collected from monitoring systems
2. Signals are segmented into fixed-size windows
3. Statistical features are extracted from each window
4. Features are passed to a trained Random Forest model
5. The model outputs:

   * probability of hypoxia
   * binary classification
   * human-readable interpretation

---

## ⚠️ Disclaimer

This project is for research and educational purposes only.
It is not intended for medical or aviation decision-making without proper validation.

---

## 📦 Model Versioning

The model is trained on statistical features extracted from physiological signals.
Ensure consistency between training features and API inputs.

---

## 👩‍💻 Author

**Agata Gabara**
Bioinformatics & Data Science student

Focused on Machine Learning in healthcare and signal-based analysis
