from pydantic import BaseModel
from uuid import UUID
from common.schema import BaseSchema

class MessageBase(BaseModel):
    thread_id: UUID
    role: str
    content: str

class MessageCreate(MessageBase):
    pass

class MessageUpdate(MessageBase):
    pass

class MessageInDBBase(MessageBase, BaseSchema):
    pass

class Message(MessageInDBBase):
    pass

class MessageInDB(MessageInDBBase):
    pass
