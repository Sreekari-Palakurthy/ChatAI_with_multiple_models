from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import relationship
from common import Base

class User(Base):
    __tablename__ = "users"
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(Integer, unique=True, index=True)
    password = Column(String)
    threads = relationship("Thread", back_populates="owner")
    key = relationship("Key", back_populates="user", uselist=False)
