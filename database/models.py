from datetime import datetime
from enum import Enum as PythonEnum

from sqlalchemy import Column, DateTime, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from .db_config import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    messages = relationship("Message", back_populates="interaction")


class MessageRole(PythonEnum):
    SYSTEM = 'system'
    HUMAN = 'human'
    AI = 'ai'


class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, index=True)
    interaction_id = Column(String, ForeignKey('interactions.id'))
    interaction = relationship("Interaction", back_populates="messages")
    created_at = Column(DateTime, default=datetime.now())
    role = Column(Enum(MessageRole))
    content = Column(String)
