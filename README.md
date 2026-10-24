# Resume Application Tracking Expert (ATS)

An ATS-style resume reviewer. Paste a job description, upload your resume as a PDF, and Gemini evaluates how well the resume fits the role.

## 🔗 Live demo

Not hosted yet. Deploy it for free on Streamlit Community Cloud: click the badge (or go to https://share.streamlit.io → **Create app**) and use repository `amitmohanty022/Resume-Application-Tracking-Expert`, branch `main`, main file `app.py`.

[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=amitmohanty022/Resume-Application-Tracking-Expert&branch=main&mainModule=app.py)

On the Streamlit deploy page, add `GOOGLE_API_KEY` under **Advanced settings → Secrets**.

## Features

- **Tell Me About the Resume:** strengths and weaknesses against the job description, written like an HR manager's review
- **Percentage match:** ATS-style match score, missing keywords and final thoughts
- The whole PDF is sent to Gemini, which reads PDFs natively, so no Poppler install is needed

## Tech stack

Python, Streamlit, Google Gen AI SDK (`google-genai`), Gemini 3.8 Flash

## Run locally

```bash
git clone https://github.com/amitmohanty022/Resume-Application-Tracking-Expert.git
cd Resume-Application-Tracking-Expert
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (or add the same keys to **Streamlit secrets** when deploying):

```env
GOOGLE_API_KEY=your_gemini_api_key   # get one at https://aistudio.google.com/apikey
# optional, defaults to gemini-3.8-flash
GEMINI_MODEL=gemini-3.8-flash
```

Then start the app:

```bash
streamlit run app.py
```

## Author

**Amit Kumar Mohanty** · [GitHub](https://github.com/amitmohanty022) · [LinkedIn](https://www.linkedin.com/in/amitkrmohanty/)
