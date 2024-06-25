from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from keys import crud, schemas
from uuid import UUID


router = APIRouter()

@router.post("/keys/", response_model=schemas.Key)
def create_key(key: schemas.KeyCreate, user_id: UUID, db: Session = Depends(get_db)):
    return crud.create_key(db=db, key=key, user_id=user_id)

@router.get("/keys/{key_id}", response_model=schemas.Key)
def read_key(key_id: UUID, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key_id=key_id)
    if db_key is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return db_key

@router.delete("/keys/{key_id}", response_model=schemas.Key)
def delete_key(key_id: UUID, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key_id=key_id)
    if db_key is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return crud.delete_key(db=db, key_id=key_id)