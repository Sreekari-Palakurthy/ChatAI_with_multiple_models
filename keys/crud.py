from sqlalchemy.orm import Session
from keys.models import Key
from keys.schemas import KeyCreate, KeyUpdate
from uuid import UUID

def get_key(db: Session, key_id: UUID):
    return db.query(Key).filter(Key.id == key_id).first()

def create_key(db: Session, key: KeyCreate, user_id: UUID):
    db_key = Key(
        anthropic_apikey=key.anthropic_apikey,
        openai_apikey=key.openai_apikey,
        mistral_apikey=key.mistral_apikey,
        user_id=user_id
    )
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key

def update_key(db: Session, key: Key, key_update: KeyUpdate):
    for key, value in key_update.dict(exclude_unset=True).items():
        setattr(key, key, value)
    db.commit()
    db.refresh(key)
    return key

def delete_key(db: Session, key_id: UUID):
    key = db.query(Key).filter(Key.id == key_id).first()
    db.delete(key)
    db.commit()
    return key
