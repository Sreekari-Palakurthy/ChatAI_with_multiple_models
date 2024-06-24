from sqlalchemy.orm import Session
from user.models import User
from user.schemas import UserCreate, UserUpdate
from uuid import UUID

def get_user(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        password=user.password  # Note: Use a password hashing library like bcrypt
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: User, user_update: UserUpdate):
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: UUID):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user
