import json
from langchain.chat_models import ChatOpenAI
from app.utils.logging import logger
import app.config as config


chatOpenAi = ChatOpenAI(
    model_name="gpt-3.5-turbo", temperature=0, openai_api_key=config.openai_api_key
)


def _convert_json(response: str):
    try:
        return json.loads(response)
    except Exception as e:
        logger.error(e)
        return {}
