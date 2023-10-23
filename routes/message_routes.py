from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
import services
from database.db_utils import get_db

router = APIRouter()


@router.post("/respond/{interaction_id}/", response_model=schemas.Message)
def respond_message(interaction_id: str,
                    message_create: schemas.MessageCreate,
                    db: Session = Depends(get_db)):
    if not services.exists_interaction(db, interaction_id):
        raise HTTPException(status_code=404, detail='Interaction Id not found!')
    ai_message = services.respond_message(db=db, interaction_id=interaction_id, human_message_create=message_create)
    if not ai_message:
        raise HTTPException(status_code=503, detail='AI Service is temporary unavailable!')
    return ai_message


@router.get("/{interaction_id}/", response_model=list[schemas.Message])
def get_messages(interaction_id: str, db: Session = Depends(get_db)):
    if not services.exists_interaction(db, interaction_id):
        raise HTTPException(status_code=404, detail='Interaction Id not found!')
    return services.get_messages(db, interaction_id)
