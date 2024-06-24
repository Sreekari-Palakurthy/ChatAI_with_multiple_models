import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Base:
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
