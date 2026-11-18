# 🎓 StudyBuddy – AI Study Assistant

Streamlit + LangChain + Groq. Meet **Mimi**, the animated doll mascot who blinks, thinks, and cheers while you study. Groq offers free API access with usage limits; check its current rate limits and model availability in your Groq account.

## Features
| Tab | What it does |
|---|---|
| 💬 Chat & Learn | Chatbot that explains difficult concepts with examples (streaming + memory). Try: *"Teach me Python loops with examples."* |
| 📅 Study Planner | Day-by-day schedule from your topic, goal, days, hours/day and start date. Downloadable. |
| 📝 MCQ Maker | Generates MCQs with hidden answers + explanations. Downloadable. |
| 🎯 Take a Quiz | Interactive quiz with scoring, review, retake, and Mimi's reactions. |

Bonus: upload PDF, TXT, or Word DOCX notes in the sidebar and every feature will use them. Uploading a file automatically selects `qwen/qwen3.8-27b`; clearing/removing it selects `openai/gpt-oss-120b`. Without an upload, the default is `openai/gpt-oss-20b`.

## Run in VS Code
1. Install Python 3.10+ and open this folder in VS Code (`File > Open Folder`).
2. Open the terminal (`Ctrl + ~`) and create a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
3. Install packages: `pip install -r requirements.txt`
4. For local use, create a `.env` file containing `GROQ_API_KEY=your_groq_api_key`. For Streamlit Community Cloud, add `GROQ_API_KEY = "your_groq_api_key"` under **App settings > Secrets**. Create a key at [console.groq.com/keys](https://console.groq.com/keys). You can also enter a different key in the sidebar's **Groq API key (optional override)** field; it applies only to your current session and takes priority over the configured key.
5. Start the app: `streamlit run app.py`
6. It opens at http://localhost:8501

The sidebar's **Model selection** section defaults to `openai/gpt-oss-20b` and includes `openai/gpt-oss-120b`. `qwen/qwen3.8-27b` is shown only while a supported study file is uploaded, and selecting a file automatically selects Qwen. Clearing or removing the upload automatically selects GPT-OSS 120B. These model IDs must be available to your Groq account.

## Structure
```
studybuddy/
├── app.py            # Streamlit UI (tabs, state, doll updates)
├── ai_engine.py      # LangChain prompts, chains, JSON quiz parsing
├── ui_theme.py       # CSS theme + Mimi SVG doll
├── requirements.txt
└── .streamlit/config.toml
```

## Troubleshooting
- **Invalid key / 403** – check or regenerate your key in the Groq console.
- **Rate limit / quota reached** – enter another Groq key in the sidebar. Select **Use configured key** to switch back.
- **App asks for an API key on Streamlit Cloud** – add `GROQ_API_KEY` under **App settings > Secrets**, or enter a key in the sidebar.
- **Model not found** – confirm the selected model is available to your Groq account.
- **Quiz failed to generate** – click the button again; the model occasionally returns malformed JSON.
- **Browser console shows Heap or `/api/v2/user/details` 404s, unsupported-feature notices, or the iframe sandbox warning** – these are emitted by the browser or Streamlit hosting page, not this app's Python code. If the app itself loads and AI requests work, they can be ignored.
