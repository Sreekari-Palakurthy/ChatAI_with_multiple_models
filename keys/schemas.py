from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class KeyBase(BaseModel):
    anthropic_apikey: Optional[str] = None
    openai_apikey: Optional[str] = None
    mistral_apikey: Optional[str] = None

class KeyCreate(KeyBase):
    anthropic_apikey: str
    openai_apikey: str
    mistral_apikey: str

class KeyUpdate(KeyBase):
    pass

class KeyInDBBase(KeyBase):
    id: UUID
    is_active: bool
    user_id: UUID

    class Config:
        orm_mode = True

class Key(KeyInDBBase):
    pass

class KeyInDB(KeyInDBBase):
    pass
