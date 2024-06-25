from pydantic import BaseModel
from uuid import UUID
from common.schema import BaseSchema

class ThreadBase(BaseModel):
    title: str
    description: str
    user_id: UUID

class ThreadCreate(ThreadBase):
    pass

class ThreadUpdate(ThreadBase):
    pass

class ThreadInDBBase(ThreadBase, BaseSchema):
    pass

class Thread(ThreadInDBBase):
    pass

class ThreadInDB(ThreadInDBBase):
    pass
