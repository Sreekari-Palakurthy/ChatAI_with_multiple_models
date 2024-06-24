from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class MessageBase(BaseModel):
    thread_id: UUID
    role: str
    content: str

class MessageCreate(BaseModel):
    thread_id: UUID
    role: str
    content: str

class MessageUpdate(MessageBase):
    pass

class Message(MessageBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
