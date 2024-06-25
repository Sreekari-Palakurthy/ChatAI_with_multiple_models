from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class BaseSchema(BaseModel):
    id:UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
