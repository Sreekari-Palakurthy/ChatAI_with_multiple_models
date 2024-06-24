from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    thread_id: UUID
    user_id: UUID

class Message(MessageBase):
    message_id: UUID
    thread_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True