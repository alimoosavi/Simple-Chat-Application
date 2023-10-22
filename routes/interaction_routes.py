from fastapi import Depends
from sqlalchemy.orm import Session

import schemas
import services
from database.db_utils import get_db
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=list[schemas.Interaction])
def get_interactions(db: Session = Depends(get_db)):
    return services.get_interactions(db)


@router.post("/", response_model=schemas.Interaction)
def create_interaction(db: Session = Depends(get_db)):
    return services.create_interaction(db)
