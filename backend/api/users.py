from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Temporary user storage
users_db = {
    1: {"id": 1, "name": "Test User", "email": "test@example.com"}
}

@router.get("/profile", response_model=UserResponse)
def get_profile():
    # For now return the test user
    return users_db[1]

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]