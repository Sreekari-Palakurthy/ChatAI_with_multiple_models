from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from common import Base
from sqlalchemy.dialects.postgresql import UUID

class Message(Base):
    __tablename__ = "messages"
    thread_id = Column(UUID(as_uuid=True), ForeignKey("threads.id"))
    role = Column(String)
    thread = relationship("Thread", back_populates="messages")
