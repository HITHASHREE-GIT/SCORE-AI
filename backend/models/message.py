from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.connection import Base


class Message(Base):

    __tablename__ = "messages"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
        nullable=False
    )


    sender = Column(
        String,
        nullable=False
    )


    content = Column(
        Text,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    # Relationship
    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )