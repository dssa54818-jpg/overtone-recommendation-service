# app/main.py (обновлено)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.recommendations import router as rec_router
from app.routes.health import router as health_router # <-- Импортируем новый роутер
from app.database import connect_db, close_db_connection # <-- Импортируем хуки БД

app = FastAPI(title="Overtone Recommendation Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация хуков для подключения/отключения от БД
@app.on_event("startup")
async def startup_event():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_connection()


app.include_router(rec_router, prefix="/recommendations", tags=["recommendations"])
# Добавляем новый роутер здоровья с префиксом /health
app.include_router(health_router, prefix="/health", tags=["health"])

@app.get("/")
async def root():
    return {"status": "ok", "message": "Recommendation service is running"}