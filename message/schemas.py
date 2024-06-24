from pydantic import BaseModel
from uuid import UUID

class MessageBase(BaseModel):
    thread_id: UUID
    role: str

class MessageCreate(MessageBase):
    pass

class MessageInDBBase(MessageBase):
    id: UUID
    is_active: bool

    class Config:
        orm_mode = True

class Message(MessageInDBBase):
    pass

class MessageInDB(MessageInDBBase):
    pass
