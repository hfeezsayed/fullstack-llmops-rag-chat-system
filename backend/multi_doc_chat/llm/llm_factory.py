from langchain_ollama import ChatOllama
from backend.multi_doc_chat.config.settings import settings
from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException
import sys


class LLMFactory:

    @staticmethod
    def get_llm():
        try:
            logger.info("Initializing Ollama LLM")

            llm = ChatOllama(
                model=settings.OLLAMA_MODEL,
                temperature=0
            )

            return llm

        except Exception as e:
            raise CustomException(e, sys)
