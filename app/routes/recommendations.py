from fastapi import APIRouter
from app.utils.logic import generate_recommendations

router = APIRouter()

@router.get("/{user_id}")
async def get_user_recommendations(user_id: str):
    recs = await generate_recommendations(user_id)
    return {"user_id": user_id, "recommendations": recs}
