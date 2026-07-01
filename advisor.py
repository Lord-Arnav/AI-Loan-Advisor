import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_advice(input_data, prediction, probability):

    status = "Approved" if prediction == 1 else "Rejected"

    prompt = f"""
    You are an experienced financial advisor.

    Applicant Details:
    {input_data}

    Loan Prediction:
    {status}

    Confidence:
    {probability[1]*100:.2f}%

    Explain:
    1. Why this decision was made.
    2. Give practical financial advice.
    3. Suggest how the applicant can improve future loan eligibility if needed.

    Keep the answer under 200 words.
    """

    response = model.generate_content(prompt)

    return response.text