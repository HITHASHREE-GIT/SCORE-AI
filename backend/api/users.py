from fastapi import APIRouter, Depends

from backend.security.dependencies import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/profile")
def profile(
    current_user = Depends(get_current_user)
):

    return {
        "message": "Profile accessed successfully",
        "email": current_user["sub"]
    }