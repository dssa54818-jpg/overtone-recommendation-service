from pydantic import BaseModel

class Recommendation(BaseModel):
    user_id: str
    track_id: str
    score: float
