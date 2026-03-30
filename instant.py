import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def welcome():
    client = OpenAI()
    message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, 
explaining that it is live on production for the first time!
"""
    # In OpenAI chat API, the role "user" is used to represent the prompts or questions provided by the end-user interacting with the assistant.
    # The instruction here is meant to be coming directly from the user (the website visitor) to the assistant, thus "user" is correct.
    # If you change this role to "system", the message would be treated as instruction to the assistant on how it should behave in the conversation,
    # typically for setting personality, tone, or behavior upfront.
    # For this use-case—requesting a reply to show to the visitor—the prompt should be from the "user":
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    return html


@app.get("/", response_class=HTMLResponse)
def about():
    return "About page"


@app.get("/health", response_class=HTMLResponse)
def health():
    return "Healthy as a horse!"
