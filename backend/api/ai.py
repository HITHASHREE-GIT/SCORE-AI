from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

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
        # Simple response for testing
        response = f"You said: '{request.message}'. This is a test response from SCORE AI!"
        return ChatResponse(response=response, success=True)
    except Exception as e:
        return ChatResponse(response=f"Error: {str(e)}", success=False)