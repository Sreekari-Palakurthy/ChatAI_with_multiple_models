from pydantic import BaseModel
from uuid import UUID

class ThreadBase(BaseModel):
    owner_id: UUID

class ThreadCreate(ThreadBase):
    pass

class ThreadInDBBase(ThreadBase):
    id: UUID
    is_active: bool

    class Config:
        orm_mode = True

class Thread(ThreadInDBBase):
    pass

class ThreadInDB(ThreadInDBBase):
    pass
