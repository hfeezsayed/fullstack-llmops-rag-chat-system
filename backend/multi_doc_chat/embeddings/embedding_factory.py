import sys

from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

from backend.multi_doc_chat.config.settings import settings
from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException


class EmbeddingFactory:

    @staticmethod
    def get_embeddings():

        try:
            provider = settings.LLM_PROVIDER.lower()

            logger.info(f"Using embedding provider: {provider}")

            if provider == "openai":
                return OpenAIEmbeddings()

            elif provider == "local":
                return HuggingFaceEmbeddings(
                    model_name=settings.EMBEDDING_MODEL
                )

            else:
                raise ValueError("Invalid embedding provider")

        except Exception as e:
            raise CustomException(e, sys)
