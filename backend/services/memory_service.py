from sqlalchemy.orm import Session

from backend.models.memory import Memory


def save_memory(
    db: Session,
    user_id: int,
    key: str,
    value: str
):

    memory = Memory(
        user_id=user_id,
        memory_key=key,
        memory_value=value
    )

    db.add(memory)
    db.commit()
    db.refresh(memory)

    return memory



def get_memory(
    db: Session,
    user_id: int,
    key: str
):

    return db.query(Memory).filter(
        Memory.user_id == user_id,
        Memory.memory_key == key
    ).first()