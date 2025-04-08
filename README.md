# 🫀 Heart Disease Prediction Project

This project uses machine learning to predict the likelihood of heart disease in patients based on various medical attributes.

## 📁 Project Structure
- `train_model.py` – Trains and evaluates Logistic Regression, Random Forest, and SVM models. The best model is saved as `models/heart_model.pkl`.
- `predict.py` – Loads the saved model and makes predictions on new patient data.
- `heart.csv` – Dataset containing patient records and heart disease labels.
- `models/` – Stores the trained model.
- `README.md` – Overview of the project.

## 🧠 Features Used for Prediction
- `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`

## 💾 Dependencies
- Python 3.x
- scikit-learn
- pandas
- numpy

Install using:
```bash
pip install -r requirements.txt
