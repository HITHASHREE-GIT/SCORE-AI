from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from ai_service import get_ai_response

router = APIRouter(prefix="/ai", tags=["ai"])


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None
    user_id: Optional[int] = 1


class ChatResponse(BaseModel):
    response: str
    success: bool


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # Send message to Groq AI
        ai_response = get_ai_response(request.message)

        return ChatResponse(
            response=ai_response,
            success=True
        )

    except Exception as e:
        return ChatResponse(
            response=f"Error: {str(e)}",
            success=False
        )