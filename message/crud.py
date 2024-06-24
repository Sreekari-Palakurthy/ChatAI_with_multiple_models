from sqlalchemy.orm import Session
from message.models import Message
from message.schemas import MessageCreate, MessageUpdate
from uuid import UUID

def get_message(db: Session, message_id: UUID):
    return db.query(Message).filter(Message.id == message_id).first()

def create_message(db: Session, message: MessageCreate):
    db_message = Message(
        thread_id=message.thread_id,
        role=message.role
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_all_thread_messages(db: Session, thread_id: UUID):
    return db.query(Message).filter(Message.thread_id == thread_id).all()

def update_message(db: Session, message: Message, message_update: MessageUpdate):
    for key, value in message_update.dict(exclude_unset=True).items():
        setattr(message, key, value)
    db.commit()
    db.refresh(message)
    return message


def delete_message(db: Session, message_id: UUID):
    message = db.query(Message).filter(Message.id == message_id).first()
    db.delete(message)
    db.commit()
    return message
