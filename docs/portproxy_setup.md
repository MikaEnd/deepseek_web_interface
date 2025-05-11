# Port Proxy Setup (WSL → Windows)

## Цель
Сделать доступным FastAPI сервер внутри WSL по адресу http://127.0.0.1:8000 из браузера Windows.

## Шаги

### 1. Получить IP-адрес WSL
```bash
ip addr show eth0 | grep inet
# Пример: 172.31.168.247
