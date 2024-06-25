from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from common.schema import BaseSchema 

class KeyBase(BaseModel):
    anthropic_apikey: Optional[str] = None
    openai_apikey: Optional[str] = None
    mistral_apikey: Optional[str] = None

class KeyCreate(KeyBase):
    anthropic_apikey: str
    openai_apikey: str
    mistral_apikey: str

class KeyUpdate(KeyBase):
    pass

class KeyInDBBase(KeyBase, BaseSchema):
    user_id: UUID

class Key(KeyInDBBase):
    pass

class KeyInDB(KeyInDBBase):
    pass
