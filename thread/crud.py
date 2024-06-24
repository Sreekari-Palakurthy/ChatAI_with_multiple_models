from sqlalchemy.orm import Session
from thread.models import Thread
from thread.schemas import ThreadCreate, ThreadUpdate
from uuid import UUID

def get_thread(db: Session, thread_id: UUID):
    return db.query(Thread).filter(Thread.id == thread_id).first()

def create_thread(db: Session, thread: ThreadCreate):
    db_thread = Thread(
        title=thread.title,
        description=thread.description,
        user_id=thread.user_id
    )
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

def get_all_threads(db: Session, user_id: UUID):
    return db.query(Thread).filter(Thread.user_id == user_id).all()

def update_thread(db: Session, thread: Thread, thread_update: ThreadUpdate):
    for key, value in thread_update.dict(exclude_unset=True).items():
        setattr(thread, key, value)
    db.commit()
    db.refresh(thread)
    return thread

def delete_thread(db: Session, thread_id: UUID):
    thread = db.query(Thread).filter(Thread.id == thread_id).first()
    db.delete(thread)
    db.commit()
    return thread
