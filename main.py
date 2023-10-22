import schemas
import crud_services as crud

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database.db_utils import create_tables, get_db

app = FastAPI()


@app.get("/interaction/", response_model=list[schemas.Interaction])
def get_interactions(db: Session = Depends(get_db)):
    return crud.get_interactions(db)


@app.post("/interaction/", response_model=schemas.Interaction)
def create_interaction(db: Session = Depends(get_db)):
    return crud.create_interaction(db)


@app.on_event("startup")
async def startup_event():
    await create_tables()
