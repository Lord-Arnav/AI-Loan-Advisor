import joblib
import pandas as pd

print("predict.py loaded")

# Load trained model
model = joblib.load("models/loan_model.pkl")


def predict_loan(input_data):
    """
    input_data should be a dictionary like:
    {
        "Gender":1,
        "Married":1,
        ...
    }
    """

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    return prediction, probability