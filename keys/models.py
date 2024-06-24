from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from common import CommonBase
from databases import Base
from sqlalchemy.dialects.postgresql import UUID

class Key(CommonBase, Base):
    __tablename__ = 'keys'
    
    anthropic_apikey = Column(String, nullable=False)
    openai_apikey = Column(String, nullable=False)
    mistral_apikey = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), unique=True)
    
    user = relationship("User", back_populates="key")