from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ThreadBase(BaseModel):
    title: str
    description: str
    user_id: UUID

class ThreadCreate(ThreadBase):
    pass

class ThreadUpdate(ThreadBase):
    pass

class Thread(ThreadBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
