from sqlalchemy.orm import Session
from user.models import User
from user.schemas import UserCreate, UserUpdate
from uuid import UUID
from datetime import datetime
import uuid

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        id=uuid.uuid4(),
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        password=hash_password(user.password),
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: User, user_update: UserUpdate):
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user

def soft_delete_user(db: Session, user_id: UUID):
    user = db.query(User).filter(User.id == user_id).first()
    user.is_active = False
    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user

def hash_password(password: str) -> str:
    return password
