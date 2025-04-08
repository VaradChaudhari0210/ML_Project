# 🫀 Heart Disease Prediction using Machine Learning

This project aims to predict the presence of heart disease in a patient based on their medical attributes using various machine learning models. The best-performing model is deployed using a simple UI powered by Streamlit.

---

## 🚀 Project Overview

Heart disease is one of the leading causes of death globally. Early detection can save lives. This project leverages machine learning to predict the likelihood of heart disease based on patient health metrics.

The workflow includes:
- Exploratory Data Analysis (EDA)
- Feature scaling
- Training multiple ML models
- Model evaluation and selection
- Deployment using Streamlit

---

## 🎯 Objective

To build and deploy a machine learning model that can accurately predict whether a patient is likely to have heart disease based on clinical and personal attributes.

---

## 📁 Project Structure

## 📁 Project Structure
- `Data`
    └── heart.csv  #Dataset
- `Notebooks`
      └── Heart_Disease_JupyterNotebook.ipynb  #Combined EDA + Model training + Prediction
- `docs`
     └── Heart_Disease_Prediction.pdfCombined #Documentation
- `models`
     └── heart_model.pkl #Trained Model(SVM)
- `src`
     └── app.py #Streamlit UI for Predictions
- `README.md` - #Project Description
- `requirements.txt` - #Required Python Packages


---

## 📊 Dataset Used

- **Source**: UCI Machine Learning Repository  
- **Filename**: `heart.csv`  
- **Features**:
  - Age, Sex, Chest Pain Type, Resting BP, Cholesterol, Fasting Blood Sugar, Rest ECG, Max Heart Rate, Exercise Angina, Oldpeak, Slope, CA, Thal
- **Target**:
  - `1` → Heart disease present  
  - `0` → No heart disease

---

## 🤖 Models Trained

- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM) ✅ (Best performing)

---

## 📈 Performance Metrics (Best Model: SVM)

- **Accuracy**: 92.2%
- **Precision**: 90.83%
- **Recall**: 94.29%
- **F1 Score**: 92.52%
- **ROC AUC**: 97.71%

---

## 🔍 Challenges & Learnings

- Handling class imbalance
- Evaluating models using multiple metrics, not just accuracy
- Improving recall to reduce false negatives
- Understanding the importance of feature scaling
- Deploying ML models using Streamlit

---

## 💻 Run Locally
Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
