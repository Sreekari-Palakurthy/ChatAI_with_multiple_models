from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from common import Base
from sqlalchemy.dialects.postgresql import UUID

class Thread(Base):
    __tablename__ = "threads"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title=Column(String)
    description=Column(String)
    owner = relationship("User", back_populates="threads")
    messages = relationship("Message", back_populates="thread")
