import schemas
import services as crud

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database.db_utils import create_tables, get_db

app = FastAPI()


@app.get("/interaction/", response_model=list[schemas.Interaction])
def get_interactions(db: Session = Depends(get_db)):
    return crud.get_interactions(db)


@app.post("/interaction/", response_model=schemas.Interaction)
def create_interaction(db: Session = Depends(get_db)):
    return crud.create_interaction(db)


@app.post("/respond/{interaction_id}/")
def respond_message(interaction_id: str, message_create: schemas.MessageCreate, db: Session = Depends(get_db)):
    if not crud.exists_interaction(db, interaction_id):
        raise HTTPException(status_code=404, detail='Interaction Id not found!')
    crud.respond_message(db=db, interaction_id=interaction_id, message_create=message_create)


@app.on_event("startup")
async def startup_event():
    await create_tables()
