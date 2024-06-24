from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime

class ThreadBase(BaseModel):
    title: str

class ThreadCreate(ThreadBase):
    created_by: UUID

class Thread(ThreadBase):
    thread_id: UUID
    created_by: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True