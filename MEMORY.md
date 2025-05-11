# MEMORY

## Backend
- [✓] FastAPI-сервер с маршрутами / и /chat
- [✓] Deepseek API интеграция через .env
- [✓] Сохранение истории сообщений в chat_history.json
- [✓] Ответы приходят с учётом предыдущего контекста

## Frontend
- [✓] Проект React инициализирован через Vite
- [✓] TailwindCSS подключён
- [✓] Запуск frontend через npm run dev --host с пробросом порта в Windows
- [✓] Реализован компонент ChatBox: история, поле ввода, отправка, загрузка, ошибки

## Инфраструктура
- [✓] Репозиторий GitHub синхронизирован через sync_github.sh
- [✓] .env подключён, ключи Deepseek скрыты
- [✓] Протокол соблюдается: nano → sync → тест → лог → memory
- [✓] React обращается к FastAPI через http://127.0.0.1:8000 (portproxy)
# Deepseek Web Interface

## Автозапуск (через systemd)

- При запуске WSL активируется systemd-сервис `deepseek.service`
- Он запускает:
  - `uvicorn` (backend API на 8000)
  - `vite` (frontend чат на 5173)

WSL запускается вручную, интерфейс работает автоматически.

# MEMORY

## systemd
- deepseek.service — запускает backend (FastAPI + Uvicorn)
- deepseek_frontend.service — запускает frontend (React + Vite)

## Порты
- 8000 — backend
- 5173 — frontend
