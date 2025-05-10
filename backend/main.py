from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.deepseek_api import ask_deepseek
from backend.history import save_message, get_messages
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "Deepseek Web Interface API running."}

@app.post("/chat")
async def chat(data: ChatRequest):
    prompt = data.prompt

    save_message("user", prompt)

    history = get_messages()
    messages = [{"role": h["role"], "content": h["content"]} for h in history]

    response = ask_deepseek(messages)
    save_message("assistant", response)

    return {"response": response}
