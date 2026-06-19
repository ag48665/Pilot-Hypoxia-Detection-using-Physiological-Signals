# 🧠 Pilot Hypoxia Detection using Physiological Signals

End-to-end machine learning project for hypoxia risk detection using physiological signal features, with a deployed FastAPI service and interactive Streamlit dashboard.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

---

## Project Overview

This project presents a machine learning system for detecting hypoxia risk using physiological signals including respiration, pulse, heart rate, and oxygen saturation.

The goal is to demonstrate how physiological time-series data can be transformed into actionable risk predictions and deployed as a production-style machine learning application.

The project combines:

* Feature engineering from physiological signals
* Machine learning classification
* FastAPI deployment
* Interactive Streamlit dashboard
* End-to-end healthcare analytics workflow

---

## Project Highlights

✔ End-to-end machine learning pipeline

✔ Physiological signal feature engineering

✔ Random Forest classification model

✔ FastAPI deployment

✔ Streamlit dashboard

✔ REST API prediction endpoint

✔ Healthcare analytics workflow

✔ Deployment-ready architecture

---

## 🌍 Live Demo

Interactive API documentation:

👉 https://pilot-hypoxia-detection-using.onrender.com/docs

---

## Main Results

* Random Forest classifier achieved approximately **95% accuracy** on the available train/test split.
* Physiological signal features successfully distinguished normal and hypoxia states.
* Respiration variability emerged as an informative predictor.
* End-to-end deployment completed using FastAPI and Streamlit.
* The model is accessible through a production-style REST API.

---

## Dataset

Source:

BIDMC Physiological Signal Dataset

https://physionet.org/content/bidmc/1.0.0/

Signals used:

* SpO₂ (oxygen saturation)
* Heart Rate (HR)
* Respiration (RESP)
* Pulse

The dataset consists of physiological time-series recordings collected from clinical monitoring systems.

The data were transformed into fixed-size windows for statistical feature extraction.

### Dataset Summary

* 108 samples
* 8 engineered features
* Binary classification task
* Normal vs hypoxia state prediction

---

## Feature Engineering

Statistical features were extracted from physiological signals using fixed-size time windows.

### Respiration Features

* Mean
* Standard deviation
* Minimum
* Maximum

### Pulse Features

* Mean
* Standard deviation

### Heart Rate Features

* Mean
* Standard deviation

These features capture physiological variability and signal dynamics rather than relying on single measurements.

---

## Machine Learning Model

### Algorithm

Random Forest Classifier

### Input Features

* resp_mean
* resp_std
* resp_min
* resp_max
* pulse_mean
* pulse_std
* hr_mean
* hr_std

### Output

The model predicts:

* Hypoxia probability
* Binary classification
* Human-readable interpretation

---

## Potential Applications

This project demonstrates how physiological signal analysis and machine learning can support early risk detection in safety-critical environments.

Potential applications include:

### Aviation Safety

* Pilot physiological monitoring
* High-altitude risk assessment
* Oxygen deprivation detection

### Healthcare Monitoring

* ICU patient monitoring
* Early respiratory deterioration detection
* Continuous physiological surveillance

### Wearable Technologies

* Smartwatch integration
* Remote health monitoring
* Real-time risk assessment

### Clinical Research

* Physiological state classification
* Predictive analytics development
* Healthcare AI research

### Human Performance Monitoring

* Fatigue monitoring
* Stress assessment
* Operational performance tracking

This project is intended for research and educational purposes and is not validated for clinical or operational deployment.

---

## System Architecture

1. Physiological signals are collected
2. Signals are segmented into fixed-size windows
3. Statistical features are extracted
4. Features are passed to a trained Random Forest model
5. The model generates:

   * Hypoxia probability
   * Binary prediction
   * Human-readable interpretation

---

## API

The trained model is deployed using FastAPI.

### Endpoint

**POST** `/predict`

### Example Request

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

### Example Response

```json
{
  "prediction": 0,
  "probability": 0.17,
  "interpretation": "NORMAL"
}
```

---

## Demo Screenshots

### FastAPI Prediction Endpoint

![API Demo](images/input_form.jpg)

![API Demo](images/response_form.jpg)

### Streamlit Dashboard

![Streamlit Demo](images/streamlit.jpg)

---

## Tech Stack

### Machine Learning

* Python
* NumPy
* Scikit-learn

### Deployment

* FastAPI
* Uvicorn
* Streamlit

### Data Processing

* WFDB
* Pandas

---

## How to Run

### Start API Server

```bash
python -m uvicorn api:app --host 127.0.0.1 --port 8001
```

### Open API Documentation

```text
http://127.0.0.1:8001/docs
```

---

## Future Improvements

* Additional physiological datasets
* Real-time monitoring pipeline
* Continuous streaming predictions
* Explainable AI (SHAP)
* Advanced feature engineering
* Model comparison and benchmarking
* Cloud deployment automation

---

## Disclaimer

This project is intended for research and educational purposes only.

It is not validated for medical diagnosis, aviation operations, or clinical decision-making.

---

## Author

**Agata Gabara**

MSc Bioinformatics Student

Interests:

* Machine Learning for Healthcare
* Clinical Informatics
* Biomedical Signal Processing
* Predictive Analytics
* Data Science for Healthcare

GitHub: https://github.com/ag48665

LinkedIn: https://www.linkedin.com/in/agatha-gabara-06494a37/
