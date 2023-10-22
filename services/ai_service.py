import schemas
import openai
from sqlalchemy.orm import Session
from typing import List
from configs.constants import OPEN_AI_API_KEY
from database.models import Interaction

openai.api_key = OPEN_AI_API_KEY


def get_session_messages(db: Session, interaction_id: str) -> List[schemas.Message]:
    db_messages = db.query(Interaction).filter(Interaction.id == interaction_id).first().messages

    return [schemas.Message(id=db_msg.id,
                            interaction_id=db_msg.interaction_id,
                            created_at=db_msg.created_at,
                            role=db_msg.role,
                            content=db_msg.content) for db_msg in db_messages]


def generate_ai_response(db: Session, interaction_id: str, content: str) -> str:
    previous_messages = [{'role': msg.role.value, 'content': msg.content}
                         for msg in get_session_messages(db=db, interaction_id=interaction_id)
                         ]
    user_message = {
        "role": "user",
        "content": content
    }
    messages = [*previous_messages, user_message]
    resp = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        temperature=0,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0,
                                        max_tokens=1000)

    return resp.get('choices')[0].get('message').get('content')
