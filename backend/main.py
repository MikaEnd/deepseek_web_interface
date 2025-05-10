from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.deepseek_api import ask_deepseek
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Deepseek Web Interface API running."}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    messages = [{"role": "user", "content": prompt}]
    response = ask_deepseek(messages)
    return {"response": response}
