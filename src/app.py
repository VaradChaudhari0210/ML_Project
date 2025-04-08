import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open("../models/heart_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load dataset and fit the scaler
df = pd.read_csv("../Data/heart.csv")
X = df.drop("target", axis=1)
scaler = StandardScaler()
scaler.fit(X)

# Define UI using Streamlit
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.title("🫀 Heart Disease Prediction App")
st.write("Fill in the patient details below to check the risk of heart disease.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=50, max_value=250, value=120)
chol = st.number_input("Serum Cholestoral in mg/dl (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results (restecg)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST depression induced by exercise (oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of the peak exercise ST segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of major vessels colored by fluoroscopy (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Predict button
if st.button("🔍 Predict"):
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]],
                              columns=X.columns)

    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1] * 100

    if prediction == 1:
        st.error("💥 Heart Disease Detected!")
    else:
        st.success("✅ No Heart Disease Detected.")

    st.metric(label="🎯 Probability of Heart Disease", value=f"{probability:.2f}%")
