from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from common.connection import SessionLocal
from user import crud, schemas
from uuid import UUID
from common.connection import get_db
from typing import List
from user.models import User
from api.openai_api import get_openai_models
from api.anthropic_api import validate_anthropic_key
from api.mistral_api import get_mistral_models

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.patch("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: UUID, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user=db_user, user_update=user_update)

@router.delete("/users/{user_id}", response_model=schemas.User)
def soft_delete_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.soft_delete_user(db=db, user_id=user_id)

@router.get("/users/models/openai", response_model=List[str])
def get_openai_models_view():
    return get_openai_models()

@router.get("/users/models/anthropic", response_model=bool)
def validate_anthropic_key_view():
    return validate_anthropic_key()

@router.get("/users/models/mistral", response_model=List[str])
def get_mistral_models_view():
    return get_mistral_models()

@router.get("/users/models/", response_model=dict)
def get_all_models():
    return {
        "openai_models": get_openai_models(),
        "mistral_models": get_mistral_models(),
        "anthropic_models": validate_anthropic_key_view()
    }