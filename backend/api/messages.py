from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/messages", tags=["messages"])

# In-memory storage
messages_db = []
message_id_counter = 1

class MessageCreate(BaseModel):
    conversation_id: int
    role: str  # "user" or "assistant"
    content: str

class MessageResponse(BaseModel):
    id: int
    conversation_id: int
    role: str
    content: str
    created_at: str

@router.post("/", response_model=MessageResponse)
def create_message(message: MessageCreate):
    global message_id_counter
    new_message = {
        "id": message_id_counter,
        "conversation_id": message.conversation_id,
        "role": message.role,
        "content": message.content,
        "created_at": datetime.now().isoformat()
    }
    messages_db.append(new_message)
    message_id_counter += 1
    return new_message

@router.get("/conversation/{conversation_id}", response_model=List[MessageResponse])
def get_messages_by_conversation(conversation_id: int):
    return [msg for msg in messages_db if msg["conversation_id"] == conversation_id]

@router.get("/", response_model=List[MessageResponse])
def get_all_messages():
    return messages_db