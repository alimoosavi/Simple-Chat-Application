from sqlalchemy.orm import Session
from utils import generate_random_str
from typing import List
from database.models import Interaction


def get_interactions(db: Session) -> List[Interaction]:
    return db.query(Interaction).all()


def exists_interaction(db: Session, interaction_id: str) -> bool:
    return db.query(Interaction).filter(Interaction.id == interaction_id).first() is not None


def create_interaction(db: Session) -> Interaction:
    db_interaction = Interaction(id=generate_random_str())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction
