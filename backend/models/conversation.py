from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database.connection import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(
        String,
        default="New Conversation"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    # Relationship with messages
    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete"
    )