# Project Summary: instant
This is a minimal Python + FastAPI web application that calls the OpenAI API on every page load and returns an AI-generated welcome message. It is wired for serverless deployment on Vercel.

# What it does
Both files define a single GET / endpoint that:

Sends a fixed prompt asking the AI to write an enthusiastic "we just launched!" announcement.
Returns the AI's reply to the browser.
File	Response format	Model used
instant.py
HTML page
gpt-4o-mini
fastapi_with_basemodel.py
JSON (message + model fields via Pydantic)
gpt-5-nano
instant.py is the active file — it is the one Vercel routes all traffic to via vercel.json.

# Tech Stack
Python 3.12
FastAPI — web framework
Uvicorn — local dev server
OpenAI SDK — AI completions
python-dotenv — loads .env for the API key
Pydantic v2 — data validation (used in the alternate file)
Vercel — serverless hosting target

# How to Run It
1. Prerequisites
Make sure you have Python 3.12 and pip (or uv) installed.

2. Install dependencies
pip install -r requirements.txt
Or with uv:

uv pip install -r requirements.txt
3. Set your OpenAI API key
Create a .env file in the project root:

OPENAI_API_KEY=sk-...your-key-here...
4. Run locally
python -m uvicorn instant:app --reload
Then open http://127.0.0.1:8000 in your browser. The page will call GPT-4o-mini and display the welcome message.

To run the alternate (JSON) version instead:

uvicorn fastapi_with_basemodel:app --reload
Then visit http://127.0.0.1:8000 — you'll get a JSON response.

5. Deploy to Vercel
vercel deploy
Make sure OPENAI_API_KEY is set as an Environment Variable in your Vercel project settings, since .env files are not uploaded.

Key note: fastapi_with_basemodel.py does not call load_dotenv(), so when running it locally you must either have OPENAI_API_KEY already set in your shell environment, or add load_dotenv() to the top of that file yourself.