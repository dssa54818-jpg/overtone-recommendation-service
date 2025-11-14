# app/database.py (обновлено)
import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

# Получение переменных окружения
# На Render вы установите MONGO_URI и DB_NAME
MONGO_URI: Optional[str] = os.environ.get("MONGO_URI")
DB_NAME: Optional[str] = os.environ.get("DB_NAME")

client: Optional[AsyncIOMotorClient] = None
db = None

if MONGO_URI and DB_NAME:
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]
else:
    # Опционально: можно добавить лог или Exception
    print("WARNING: MONGO_URI or DB_NAME not set. Database connection will be unavailable.")

async def check_db_connection() -> bool:
    """Проверяет работоспособность подключения к MongoDB (пингует сервер)."""
    if client is None:
        return False
    try:
        # Команда ping для проверки подключения к БД
        await client.admin.command('ping')
        return True
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return False

# Добавьте эти функции в main.py для корректного закрытия соединения
async def connect_db():
    if client:
        await client.get_io_loop() # Обеспечивает инициализацию
        print("MongoDB connected successfully.")

async def close_db_connection():
    if client:
        client.close()
        print("MongoDB connection closed.")