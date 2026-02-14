import sys
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.multi_doc_chat.config.settings import settings
from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException


class EmbeddingFactory:

    @staticmethod
    def get_embeddings():
        try:
            provider = settings.EMBEDDING_PROVIDER.lower()

            logger.info(f"Initializing embedding provider: {provider}")

            if provider == "huggingface":
                embeddings = HuggingFaceEmbeddings(
                    model_name=settings.EMBEDDING_MODEL
                )
                return embeddings

            else:
                raise ValueError("Invalid embedding provider")

        except Exception as e:
            raise CustomException(e, sys)
