from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class KeyBase(BaseModel):
    anthropic_apikey: str
    openai_apikey: str
    mistral_apikey: str

class KeyCreate(KeyBase):
    user_id: UUID

class Key(KeyBase):
    key_id: UUID
    user_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True