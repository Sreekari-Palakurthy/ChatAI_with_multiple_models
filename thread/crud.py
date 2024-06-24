from sqlalchemy.orm import Session
from .models import Thread
from .schemas import ThreadCreate
from uuid import UUID

def get_thread(db: Session, thread_id: UUID):
    return db.query(Thread).filter(Thread.id == thread_id).first()

def create_thread(db: Session, thread: ThreadCreate):
    db_thread = Thread(
        owner_id=thread.owner_id
    )
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

def delete_thread(db: Session, thread_id: UUID):
    thread = db.query(Thread).filter(Thread.id == thread_id).first()
    db.delete(thread)
    db.commit()
    return thread
