# Resume Application Tracking Expert (ATS)

Upload your resume as a PDF, paste a job description, and Google Gemini will either:

- **Tell Me About the Resume**: review strengths and weaknesses against the job, like an HR manager would.
- **Percentage match**: score the resume like an ATS, list missing keywords, and give final thoughts.

## How to run (step by step)

You need **Python 3.10 or newer** ([download](https://www.python.org/downloads/)).

**1. Download the project**

```bash
git clone https://github.com/amitmohanty022/Resume-Application-Tracking-Expert.git
cd Resume-Application-Tracking-Expert
```

**2. Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

**3. Install the requirements**

```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

- Get a free key at https://aistudio.google.com/apikey
- Copy `.env.example` to a new file named `.env`
  - Windows: `copy .env.example .env`
  - macOS / Linux: `cp .env.example .env`
- Open `.env` and paste your key after `GOOGLE_API_KEY=`

**5. Start the app**

```bash
streamlit run app.py
```

Your browser opens at http://localhost:8501.

**6. Use it**

1. Paste the job description in the text box.
2. Upload your resume (PDF).
3. Click one of the two buttons.

## How it works

The PDF is sent directly to Gemini (`gemini-3.8-flash` by default), which reads every page. No extra software such as Poppler is needed. To use a different model, set `GEMINI_MODEL` in `.env`.

## Troubleshooting

| Problem | Fix |
|---|---|
| "GOOGLE_API_KEY is not set" | Make sure the file is named exactly `.env` (not `.env.txt`) and is in the project folder. |
| `streamlit: command not found` | Activate the virtual environment (step 2) first. |
| `404 model not found` | Set `GEMINI_MODEL=gemini-3.6-flash` in `.env`. |
