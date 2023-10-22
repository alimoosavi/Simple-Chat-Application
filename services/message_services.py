import schemas
from sqlalchemy.orm import Session
from .ai_service import generate_ai_response


def respond_message(db: Session, interaction_id: str, message_create: schemas.MessageCreate):
    generate_ai_response(db=db, interaction_id=interaction_id, content=message_create.content)
