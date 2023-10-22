from pydantic import BaseModel
from datetime import datetime
from typing import List, Union
from database.models import MessageStatus


class Message(BaseModel):
    id: str
    created_at: datetime
    role: MessageStatus
    content: str

    class Config:
        orm_mode = True


class Interaction(BaseModel):
    id: str
    created_at: datetime
    updated_at: Union[datetime, None] = None
    messages: List[Message] = []

    class Config:
        orm_mode = True


class InteractionCreate(BaseModel):
    pass
