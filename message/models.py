from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    thread_id = Column(UUID(as_uuid=True), ForeignKey('threads.thread_id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    thread = relationship("Thread", back_populates="messages")
    sender = relationship("User", back_populates="messages")