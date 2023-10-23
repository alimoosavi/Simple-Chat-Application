import schemas
from sqlalchemy.orm import Session
from typing import List, Union
from database.models import Message, MessageRole
from .ai_service import generate_ai_response, ChatGPTException
from utils import generate_random_str
from datetime import datetime


def respond_message(db: Session, interaction_id: str, human_message_create: schemas.MessageCreate) -> \
        Union[Message | None]:
    try:
        ai_content = generate_ai_response(db=db,
                                          interaction_id=interaction_id,
                                          content=human_message_create.content)
    except ChatGPTException:
        return None
    human_message = Message(id=generate_random_str(),
                            content=human_message_create.content,
                            role=MessageRole.HUMAN,
                            interaction_id=interaction_id,
                            created_at=datetime.now())
    ai_message = Message(id=generate_random_str(),
                         content=ai_content,
                         role=MessageRole.AI,
                         interaction_id=interaction_id,
                         created_at=datetime.now())

    db.add(human_message)
    db.add(ai_message)
    db.commit()

    db.refresh(ai_message)
    return ai_message


def get_messages(db: Session, interaction_id: str) -> List[Message]:
    return db.query(Message).filter(Message.interaction_id == interaction_id).all()
