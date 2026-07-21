from fastapi import APIRouter

router = APIRouter(prefix="/routes", tags=["routes"])

@router.get("/")
def get_routes():
    return {
        "routes": [
            "/auth/register",
            "/auth/login",
            "/conversations",
            "/conversations/{id}",
            "/messages",
            "/messages/conversation/{id}"
        ]
    }