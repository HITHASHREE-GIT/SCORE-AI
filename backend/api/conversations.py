from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/conversations", tags=["conversations"])

# In-memory storage
conversations_db = []
conversation_id_counter = 1

class ConversationCreate(BaseModel):
    title: str
    user_id: int

class ConversationResponse(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: str
    updated_at: str

@router.post("/", response_model=ConversationResponse)
def create_conversation(conversation: ConversationCreate):
    global conversation_id_counter
    now = datetime.now().isoformat()
    new_conversation = {
        "id": conversation_id_counter,
        "title": conversation.title,
        "user_id": conversation.user_id,
        "created_at": now,
        "updated_at": now
    }
    conversations_db.append(new_conversation)
    conversation_id_counter += 1
    return new_conversation

@router.get("/", response_model=List[ConversationResponse])
def get_conversations():
    return conversations_db

@router.get("/{conversation_id}", response_model=ConversationResponse)
def get_conversation(conversation_id: int):
    for conv in conversations_db:
        if conv["id"] == conversation_id:
            return conv
    raise HTTPException(status_code=404, detail="Conversation not found")