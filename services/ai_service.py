from typing import List

import openai
from sqlalchemy.orm import Session

import schemas
from configs.constants import (OPEN_AI_API_KEY,
                               OPEN_AI_CHAT_CONFIG_MODEL,
                               OPEN_AI_CHAT_CONFIG_TEMPERATURE,
                               OPEN_AI_CHAT_CONFIG_TOP_P,
                               OPEN_AI_CHAT_CONFIG_FREQUENCY_PENALTY,
                               OPEN_AI_CHAT_CONFIG_PRESENCE_PENALTY,
                               OPEN_AI_CHAT_CONFIG_MAX_TOKENS)
from database.models import Interaction

openai.api_key = OPEN_AI_API_KEY
OPEN_AI_CHAT_CONFIG = {
    'model': OPEN_AI_CHAT_CONFIG_MODEL,
    'temperature': OPEN_AI_CHAT_CONFIG_TEMPERATURE,
    'top_p': OPEN_AI_CHAT_CONFIG_TOP_P,
    'frequency_penalty': OPEN_AI_CHAT_CONFIG_FREQUENCY_PENALTY,
    'presence_penalty': OPEN_AI_CHAT_CONFIG_PRESENCE_PENALTY,
    'max_tokens': OPEN_AI_CHAT_CONFIG_MAX_TOKENS
}


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
    resp = openai.ChatCompletion.create(messages=messages,
                                        **OPEN_AI_CHAT_CONFIG)

    return resp.get('choices')[0].get('message').get('content')
