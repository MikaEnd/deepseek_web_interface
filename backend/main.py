from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/")
async def root():
    return {"message": "Deepseek Web Interface API running."}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    # Сохраняем сообщение пользователя
    save_message("user", prompt)

    # Загружаем всю историю
    history = get_messages()
    messages = [{"role": h["role"], "content": h["content"]} for h in history]

    # Отправляем полный контекст в Deepseek
    response = ask_deepseek(messages)

    # Сохраняем ответ ИИ
    save_message("assistant", response)

    return {"response": response}
