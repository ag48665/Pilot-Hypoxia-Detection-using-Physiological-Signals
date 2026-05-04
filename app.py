import streamlit as st
import joblib
import numpy as np

model = joblib.load("hypoxia_model.pkl")

st.set_page_config(
    page_title="Pilot Hypoxia Detection",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Pilot Hypoxia Detection")
st.write("Predict hypoxia risk based on physiological signal features.")

st.divider()

resp_mean = st.number_input("Respiration mean", value=18.0)
resp_std = st.number_input("Respiration std", value=2.0)
resp_min = st.number_input("Respiration min", value=14.0)
resp_max = st.number_input("Respiration max", value=22.0)

pulse_mean = st.number_input("Pulse mean", value=75.0)
pulse_std = st.number_input("Pulse std", value=5.0)

hr_mean = st.number_input("Heart rate mean", value=78.0)
hr_std = st.number_input("Heart rate std", value=6.0)

st.divider()

if st.button("Predict hypoxia risk"):
    values = np.array([[
        resp_mean,
        resp_std,
        resp_min,
        resp_max,
        pulse_mean,
        pulse_std,
        hr_mean,
        hr_std
    ]])

    prediction = model.predict(values)[0]
    probability = model.predict_proba(values)[0][1]

    st.subheader("Prediction result")

    if prediction == 1:
        st.error("⚠️ HYPOXIA RISK")
    else:
        st.success("✅ NORMAL")

    st.metric("Hypoxia probability", f"{probability:.2f}")

st.divider()

st.caption(
    "Research and educational project. Not intended for medical or aviation decision-making."
)