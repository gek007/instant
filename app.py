from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str
    model: str


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def instant():
    client = OpenAI()
    message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
"""
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content

    # Render the response as beautiful HTML text
    html_content = f"""
    <html>
        <head>
            <title>Welcome Announcement</title>
            <style>
                body {{
                    background: linear-gradient(135deg, #f0f6fc, #ffe7d6 120%);
                    font-family: 'Segoe UI', 'Arial', sans-serif;
                    display: flex;
                    flex-direction: column;
                    min-height: 100vh;
                }}
                .container {{
                    max-width: 600px;
                    margin: 80px auto 0 auto;
                    background: white;
                    border-radius: 20px;
                    box-shadow: 0 6px 24px rgba(80,40,40,0.15);
                    padding: 44px 36px;
                    text-align: center;
                }}
                h1 {{
                    color: #2f80ed;
                    margin-bottom: 18px;
                    letter-spacing: 0.02em;
                    font-size: 2.6em;
                }}
                p {{
                    color: #23272f;
                    font-size: 1.4em;
                    line-height: 1.7;
                }}
                .model {{
                    color: #888;
                    font-size: 0.96em;
                    margin-top: 16px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 Kostya, Welcome!</h1>
                <p>{reply.replace("\n", "<br/>")}</p>
                <div class="model">🤖 Powered by: <b>gpt-5-nano</b></div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/hello")
def hello():
    return {"message": "Hello, Kostya! Welcome to the site!"}
