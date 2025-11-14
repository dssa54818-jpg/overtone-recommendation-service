# app/database.py
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DB_NAME")

client = None
db = None

if MONGO_URI and DB_NAME:
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]

async def check_db_connection() -> bool:
    """Проверяет работоспособность подключения к MongoDB Atlas."""
    if not client:
        return False
    try:
        # Отправляем команду ping для проверки соединения
        await client.admin.command('ping')
        return True
    except Exception:
        return False

# Функции для startup/shutdown (нужны для main.py)
async def connect_db():
    # [Добавьте логику подключения]
    pass # Упрощенно, Motor подключается при первом запросе

async def close_db_connection():
    if client:
        client.close()
