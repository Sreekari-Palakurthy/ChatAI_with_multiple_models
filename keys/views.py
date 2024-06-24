from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from databases import get_db
from crud import create_key
from schemas import KeyCreate, Key as KeySchema

router = APIRouter()

@router.post("/keys/", response_model=KeySchema)
async def create_key_view(key: KeyCreate, db: AsyncSession = Depends(get_db)):
    return await create_key(db, key)