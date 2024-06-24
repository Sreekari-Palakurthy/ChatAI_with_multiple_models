from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime


class KeyBase(BaseModel):
    key_value: str

class KeyCreate(KeyBase):
    user_id: UUID

class Key(KeyBase):
    key_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True