import httpx
from app.database import db

async def get_reviews_from_review_service(user_id: str):
    """
    Пример: обращаемся к микросервису рецензий
    (пока он фейковый, потом подставим реальный адрес)
    """
    REVIEW_SERVICE_URL = "http://review-service:8000/reviews/user"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{REVIEW_SERVICE_URL}/{user_id}")
            return response.json()
    except Exception:
        return []

async def generate_recommendations(user_id: str):
    reviews = await get_reviews_from_review_service(user_id)
    if not reviews:
        return []

    recs = []
    for review in reviews:
        if review.get("rating", 0) > 8:
            recs.append({
                "user_id": user_id,
                "track_id": review["track_id"],
                "title": review.get("title", "Unknown Track"),
                "artist": review.get("artist", "Unknown Artist"),
                "score": review["rating"],
                "reason": review.get("text", "")
            })
    return recs

