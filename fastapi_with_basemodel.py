from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str
    model: str


app = FastAPI()


@app.get("/", response_model=MessageResponse)
def instant():
    client = OpenAI()
    message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
"""
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")

    # return JSON response
    # return {
    #     "message": reply
    #     "model": "gpt-5-nano"
    # }

    return MessageResponse(message=reply, model="gpt-5-nano")
