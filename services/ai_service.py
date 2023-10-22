import openai
from sqlalchemy.orm import Session
from configs.constants import OPEN_AI_API_KEY
from database.models import Interaction

openai.api_key = OPEN_AI_API_KEY


def get_session_messages(db: Session, interaction_id: str):
    return db.query(Interaction).filter(Interaction.id == interaction_id).first().messages


def generate_ai_response(db: Session, interaction_id: str, content: str):
    user_message = {
        "role": "user",
        "content": content
    }
    messages = [*get_session_messages(db=db, interaction_id=interaction_id), user_message]
    resp = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        temperature=0,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0,
                                        max_tokens=1000)
    ai_message = resp.get('choices')[0].get('message')
    messages.append(ai_message)
