import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

st.set_page_config(page_title="Resume Application Tracking Expert")
st.header("Resume Tracking System")

if not API_KEY:
    st.error("GOOGLE_API_KEY is not set. Copy .env.example to .env and paste your Gemini API key.")
    st.stop()

client = genai.Client(api_key=API_KEY)


def get_gemini_response(instructions, pdf_part, job_description):
    contents = [instructions, pdf_part, f"Job Description:\n{job_description or '(not provided)'}"]
    response = client.models.generate_content(model=MODEL, contents=contents)
    return response.text


def input_pdf_setup(uploaded_file):
    """Send the whole PDF to Gemini; it reads PDFs natively (all pages)."""
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")
    return types.Part.from_bytes(data=uploaded_file.getvalue(), mime_type="application/pdf")


input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description.
  Please share your professional evaluation on whether the candidate's profile aligns with the role.
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1 or submit3:
    if uploaded_file is None:
        st.write("Please upload the resume")
    else:
        prompt = input_prompt1 if submit1 else input_prompt3
        with st.spinner("Analyzing resume..."):
            response = get_gemini_response(prompt, input_pdf_setup(uploaded_file), input_text)
        st.subheader("The Response is")
        st.write(response)
