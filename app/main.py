# app/main.py (обновлено)
from fastapi import FastAPI
# ... другие импорты ...
from app.routes.recommendations import router as rec_router
from app.routes.health import router as health_router # <-- Новый импорт
from app.database import connect_db, close_db_connection 

app = FastAPI(title="Overtone Recommendation Service")

# ... app.add_middleware ...

@app.on_event("startup")
async def startup_event():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_connection()

app.include_router(rec_router, prefix="/recommendations", tags=["recommendations"])
app.include_router(health_router, prefix="/health", tags=["health"]) # <-- Регистрация роутера здоровья

@app.get("/")
async def root():
# ...
