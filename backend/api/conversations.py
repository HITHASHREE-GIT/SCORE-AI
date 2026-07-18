from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.models.conversation import Conversation
from backend.schemas.conversation_schema import (
    ConversationCreate,
    ConversationResponse
)
from backend.security.dependencies import get_current_user


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.post("/", response_model=ConversationResponse)
def create_conversation(
    data: ConversationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    conversation = Conversation(
        title=data.title,
        user_id=current_user["id"]
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


@router.get("/", response_model=list[ConversationResponse])
def get_conversations(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    conversations = db.query(Conversation).filter(
        Conversation.user_id == current_user["id"]
    ).all()

    return conversations