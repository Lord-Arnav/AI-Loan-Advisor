from predict import predict_loan

sample = {
    "Gender": 1,
    "Married": 1,
    "Dependents": 0,
    "Education": 1,
    "Self_Employed": 0,
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 2000,
    "LoanAmount": 150,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": 2
}

prediction, probability = predict_loan(sample)

print("Prediction:", prediction)
print("Probability:", probability)