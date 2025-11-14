# app/routes/health.py
from fastapi import APIRouter, HTTPException
from app.database import check_db_connection

router = APIRouter()

@router.get("/db")
async def db_health_check():
    """Проверяет подключение к MongoDB Atlas."""
    if await check_db_connection():
        return {"status": "ok", "database": "MongoDB Atlas", "connection": "successful"}
    
    # Если подключение не удалось, возвращаем ошибку 503
    raise HTTPException(status_code=503, detail="Database connection failed")