import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def get_api_key():
    """Read the Gemini API key from Streamlit secrets or the environment."""
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        pass
    return os.getenv("GOOGLE_API_KEY")


MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def get_gemini_response(input_prompt, pdf_content, job_description):
    client = genai.Client(api_key=get_api_key())
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[input_prompt, pdf_content[0], job_description],
    )
    return response.text


def input_pdf_setup(uploaded_file):
    """Send the whole PDF to Gemini, which reads PDFs natively (no Poppler needed)."""
    if uploaded_file is not None:
        return [types.Part.from_bytes(data=uploaded_file.getvalue(), mime_type="application/pdf")]
    raise FileNotFoundError("No file uploaded")


## Streamlit App

st.set_page_config(page_title="Resume Application Tracking Expert")
st.header("Resume Tracking System")
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


def run(prompt):
    if not get_api_key():
        st.error("GOOGLE_API_KEY is not set. Add it to a .env file or to Streamlit secrets.")
    elif uploaded_file is None:
        st.write("Please upload the resume")
    else:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(prompt, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)


if submit1:
    run(input_prompt1)
elif submit3:
    run(input_prompt3)
