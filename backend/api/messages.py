from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.connection import get_db

from backend.models.message import Message
from backend.models.conversation import Conversation

from backend.schemas.message_schema import (
    MessageCreate,
    MessageResponse
)

from backend.security.dependencies import get_current_user

from backend.agents.ai_agent import generate_ai_response


router = APIRouter(
    prefix="/conversations",
    tags=["Messages"]
)


@router.post("/{conversation_id}/messages")
def send_message(
    conversation_id: int,
    data: MessageCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    # Check conversation ownership

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user["id"]
    ).first()


    if not conversation:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )


    # Save user message

    user_message = Message(
        conversation_id=conversation_id,
        sender="user",
        content=data.content
    )


    db.add(user_message)
    db.commit()
    db.refresh(user_message)



    # Generate AI response

    ai_reply = generate_ai_response(
        data.content
    )



    # Save AI message

    ai_message = Message(
        conversation_id=conversation_id,
        sender="ai",
        content=ai_reply
    )


    db.add(ai_message)
    db.commit()
    db.refresh(ai_message)



    # Clean JSON response

    return {

        "conversation_id": conversation_id,

        "user_message": {
            "id": user_message.id,
            "sender": user_message.sender,
            "content": user_message.content,
            "created_at": user_message.created_at
        },


        "ai_message": {
            "id": ai_message.id,
            "sender": ai_message.sender,
            "content": ai_message.content,
            "created_at": ai_message.created_at
        }

    }