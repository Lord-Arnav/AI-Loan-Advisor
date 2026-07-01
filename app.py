import streamlit as st
from predict import predict_loan
from advisor import get_advice

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Loan Approval Advisor",
    page_icon="🏦",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("🏦 AI Loan Approval & Financial Advisor")

st.markdown("""
Welcome! This application predicts whether a loan is likely to be approved using a **Machine Learning model**
and then provides **personalized financial advice** using **Google Gemini AI**.
""")

st.divider()

# ---------------- INPUT SECTION ---------------- #

st.subheader("📝 Applicant Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "👤 Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "💍 Married",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "👨‍👩‍👧 Dependents",
        [0, 1, 2, 3]
    )

    education = st.selectbox(
        "🎓 Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "💼 Self Employed",
        ["Yes", "No"]
    )

with col2:

    applicant_income = st.number_input(
        "💰 Applicant Income",
        min_value=0
    )

    coapplicant_income = st.number_input(
        "💵 Co-applicant Income",
        min_value=0
    )

    loan_amount = st.number_input(
        "🏦 Loan Amount",
        min_value=0
    )

    loan_term = st.number_input(
        "📅 Loan Term (Months)",
        value=360
    )

    credit_history = st.selectbox(
        "📈 Credit History",
        [1, 0],
        format_func=lambda x: "Good" if x == 1 else "Bad"
    )

    property_area = st.selectbox(
        "🏠 Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

st.write("")

predict = st.button(
    "🔍 Predict Loan Approval",
    use_container_width=True
)

# ---------------- PREDICTION ---------------- #

if predict:

    input_data = {
        "Gender": 1 if gender == "Male" else 0,
        "Married": 1 if married == "Yes" else 0,
        "Dependents": dependents,
        "Education": 0 if education == "Graduate" else 1,
        "Self_Employed": 1 if self_employed == "Yes" else 0,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": {
            "Rural": 0,
            "Semiurban": 1,
            "Urban": 2
        }[property_area]
    }

    prediction, probability = predict_loan(input_data)

    st.divider()

    st.subheader("📊 Prediction Result")

    result_col1, result_col2 = st.columns([2, 1])

    with result_col1:

        if prediction == 1:
            st.success("🎉 Congratulations! Your loan is likely to be Approved.")
        else:
            st.error("⚠️ Your loan is likely to be Rejected.")

    with result_col2:

        st.metric(
            label="Approval Probability",
            value=f"{probability[1]*100:.2f}%"
        )

    advice = get_advice(
        input_data,
        prediction,
        probability
    )

    st.divider()

    with st.expander("🤖 AI Financial Advisor", expanded=True):
        st.write(advice)

# ---------------- FOOTER ---------------- #

st.divider()

st.caption(
    "Developed by Arnav Thapliyal | Python • Streamlit • Scikit-learn • Google Gemini AI"
)