from fastapi import APIRouter


router = APIRouter(
    tags=["General"]
)


@router.get("/status")
def status():

    return {
        "message": "SCORE AI API is running",
        "status": "active"
    }