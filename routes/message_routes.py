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
    return services.respond_message(db=db, interaction_id=interaction_id, human_message_create=message_create)
