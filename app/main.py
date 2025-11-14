# app/main.py (Исправлено)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Импортируем роутеры
from app.routes.recommendations import router as rec_router
from app.routes.health import router as health_router # <-- Новый импорт для /health
# Импортируем функции БД
from app.database import connect_db, close_db_connection 

app = FastAPI(title="Overtone Recommendation Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Хуки для подключения/отключения от БД
@app.on_event("startup")
async def startup_event():
    # Тело функции должно быть индетировано
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    # Тело функции должно быть индетировано
    await close_db_connection()


# 2. Регистрация роутеров
app.include_router(rec_router, prefix="/recommendations", tags=["recommendations"])
app.include_router(health_router, prefix="/health", tags=["health"]) # <-- Регистрация роутера здоровья

# 3. Базовый эндпоинт
@app.get("/")
async def root():
    # Тело функции должно быть индетировано
    return {"status": "ok", "message": "Recommendation service is running"}
