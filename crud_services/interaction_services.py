from sqlalchemy.orm import Session
from utils import generate_random_str
from database.models import Interaction


def get_interactions(db: Session):
    return db.query(Interaction).all()


def create_interaction(db: Session):
    db_interaction = Interaction(id=generate_random_str())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction
