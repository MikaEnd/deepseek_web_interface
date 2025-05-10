import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("chat_history.json")

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_message(role, content):
    history = load_history()
    history.append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    })
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def get_messages():
    return load_history()
