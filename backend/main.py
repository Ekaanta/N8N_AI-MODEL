from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import requests

app = FastAPI()

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/process-article"

class ArticleRequest(BaseModel):
    email: str
    article_url: str

@app.get("/")
def home():
    return {"message": "AI Agent Backend Running successfully!"}

@app.post("/submit")
def submit(data: ArticleRequest):
    session_id = str(uuid.uuid4())

    payload = {
        "email": data.email,
        "article_url": data.article_url,
        "session_id": session_id
    }

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
        n8n_status = response.status_code
    except Exception as e:
        n8n_status = f"error: {str(e)}"

    return {
        "status": "success",
        "session_id": session_id,
        "email": data.email,
        "article_url": data.article_url,
        "n8n_status": n8n_status
    }