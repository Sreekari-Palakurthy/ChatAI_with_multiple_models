from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from message import crud, schemas
from uuid import UUID
from typing import List
from dependencies import get_db

router = APIRouter()

@router.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@router.get("/messages/{message_id}", response_model=schemas.Message)
def read_message(message_id: UUID, db: Session = Depends(get_db)):
    db_message = crud.get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@router.post("/messages/thread/{thread_id}", response_model=List[schemas.Message])
def get_all_thread_messages(thread_id: UUID, db: Session = Depends(get_db)):
    db_messages = crud.get_all_thread_messages(db, thread_id=thread_id)
    if not db_messages:
        raise HTTPException(status_code=404, detail="No messages found for this thread")
    return db_messages