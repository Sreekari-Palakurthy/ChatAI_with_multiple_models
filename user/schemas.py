from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: int

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    name: str = None
    email: EmailStr = None
    phone_number: str = None

class User(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
