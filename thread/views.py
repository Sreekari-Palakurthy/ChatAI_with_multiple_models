from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from thread import crud, schemas
from uuid import UUID
from typing import List
from common_app.dependencies import get_db

router = APIRouter()


@router.post("/threads/", response_model=schemas.Thread)
def create_thread(thread: schemas.ThreadCreate, db: Session = Depends(get_db)):
    return crud.create_thread(db=db, thread=thread)

@router.get("/threads/{thread_id}", response_model=schemas.Thread)
def read_thread(thread_id: UUID, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return db_thread

@router.get("/threads/user/{user_id}", response_model=List[schemas.Thread])
def get_all_threads(user_id: UUID, db: Session = Depends(get_db)):
    db_threads = crud.get_all_threads(db, user_id=user_id)
    if not db_threads:
        raise HTTPException(status_code=404, detail="No threads found for this user")
    return db_threads

@router.delete("/threads/{thread_id}", response_model=schemas.Thread)
def delete_thread(thread_id: UUID, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return crud.delete_thread(db=db, thread_id=thread_id)
