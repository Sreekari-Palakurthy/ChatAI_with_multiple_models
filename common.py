import uuid
from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.sql import func

def generate_uuid():
    return str(uuid.uuid4())

class CommonBase:
    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=generate_uuid, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
