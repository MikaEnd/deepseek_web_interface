from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "./frontend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/chat_file")
async def chat_file(prompt: str = Form(...), file: UploadFile = File(None)):
    if file:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 👇 вернём путь к изображению в URL-формате
        return JSONResponse(content={
            "response": "Изображение успешно загружено!",
            "file_url": f"/uploads/{file.filename}"
        })

    # если только текст
    return JSONResponse(content={"response": f"Вы написали: {prompt}"})
