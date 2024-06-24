from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from common import Base
from sqlalchemy.dialects.postgresql import UUID

class Key(Base):
    __tablename__ = "keys"
    anthropic_apikey = Column(String)
    openai_apikey = Column(String)
    mistral_apikey = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship("User", back_populates="key")
