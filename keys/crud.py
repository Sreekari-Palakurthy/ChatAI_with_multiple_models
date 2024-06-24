from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from ..models import Key
from ..schemas import KeyCreate, Key as KeySchema

async def create_key(db: AsyncSession, key: KeyCreate) -> KeySchema:
    db_key = Key(anthropic_apikey=key.anthropic_apikey, openai_apikey=key.openai_apikey, mistral_apikey=key.mistral_apikey, user_id=key.user_id)
    db.add(db_key)
    try:
        await db.commit()
        await db.refresh(db_key)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Key already exists for this user")
    return db_key