from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseSchema(BaseModel):
    id: Optional[UUID]
    is_active: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
