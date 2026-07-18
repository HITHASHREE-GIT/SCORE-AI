from sqlalchemy import Column, Integer, String, Text, ForeignKey
from backend.database.connection import Base


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    memory_key = Column(
        String,
        nullable=False
    )

    memory_value = Column(
        Text,
        nullable=False
    )