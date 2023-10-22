from pydantic import BaseModel
from datetime import datetime
from typing import List, Union
from database.models import MessageRole


class Message(BaseModel):
    id: str
    interaction_id: str
    created_at: datetime
    role: MessageRole
    content: str

    class Config:
        orm_mode = True


class MessageCreate(BaseModel):
    content: str


class Interaction(BaseModel):
    id: str
    created_at: datetime
    updated_at: Union[datetime, None] = None
    messages: List[Message] = []

    class Config:
        orm_mode = True
