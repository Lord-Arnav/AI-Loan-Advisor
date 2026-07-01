# 🏦 AI Loan Approval & Financial Advisor

An AI-powered web application that predicts whether a loan application is likely to be approved using Machine Learning and provides personalized financial advice using Google's Gemini AI.

---

## 📌 Project Overview

This project combines **Machine Learning** and **Generative AI** to help users understand their loan approval chances.

The application:
- Predicts loan approval using a trained Random Forest model.
- Displays the approval probability.
- Uses Gemini AI to explain the prediction in simple language.
- Provides personalized financial advice based on the applicant's details.

---

## 🚀 Features

- 📊 Loan Approval Prediction
- 🤖 AI Financial Advisor (Gemini AI)
- 📈 Approval Probability
- 🧹 Data Cleaning & Preprocessing
- 🌐 Interactive Streamlit Web App
- 💾 Saved Machine Learning Model
- 🔒 Secure API Key using `.env`

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### AI
- Google Gemini API

### Web Framework
- Streamlit

### Model Storage
- Joblib

### Visualization
- Matplotlib

---

## 📂 Project Structure

```
AI Loan Advisor/
│
├── app.py                 # Streamlit application
├── advisor.py             # Gemini AI integration
├── predict.py             # Prediction logic
├── test_predict.py        # Testing prediction module
│
├── data/
│   └── Loan-Approval-Prediction.csv
│
├── models/
│   └── loan_model.pkl
│
├── notebooks/
│   └── loan_analysis.ipynb
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Loan-Advisor.git
```

### Open the project

```bash
cd AI-Loan-Advisor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Encode Categorical Features
5. Train-Test Split
6. Train Random Forest Classifier
7. Save Model using Joblib
8. Predict Loan Approval
9. Generate AI Financial Advice using Gemini

---

## 📊 Model Performance

Algorithm Used:

- Random Forest Classifier

Current Accuracy:

- **75.6%**

---

## 📷 Application Screenshots

Add screenshots here after deployment.

Example:

```
Home Screen

Prediction Result

AI Financial Advice
```

---

## 🔮 Future Improvements

- PDF Loan Report
- Feature Importance Graph
- Better UI/UX
- Prediction History
- SHAP Explainability
- Deploy on Streamlit Cloud

---

## Author

**Arnav Thapliyal**
