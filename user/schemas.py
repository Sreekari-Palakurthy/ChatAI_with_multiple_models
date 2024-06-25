from pydantic import BaseModel,EmailStr
from uuid import UUID
from common.schema import BaseSchema


class UserBase(BaseSchema):
    name:str
    email: EmailStr
    phone_number: int

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password:str

class User(UserBase):
    id: UUID
    name: str
    email: EmailStr
    phone_number: int

    class Config:
        orm_mode = True

class ModelDescription(BaseModel):
    name: str
    description: str