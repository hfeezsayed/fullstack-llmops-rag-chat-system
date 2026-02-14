from backend.multi_doc_chat.vectorstore.faiss_store import FAISSVectorStore
from backend.multi_doc_chat.embeddings.embedding_factory import EmbeddingFactory
from backend.multi_doc_chat.retriever.retriever import Retriever
from backend.multi_doc_chat.llm.llm_factory import LLMFactory
from backend.multi_doc_chat.llm.response_generator import ResponseGenerator

from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException

import sys


class ChatService:
    def __init__(self):
        try:
            logger.info("Initializing Chat Service...")

            # 1. Load embeddings
            self.embedding_model = EmbeddingFactory.get_embeddings()

            # 2. Load FAISS vector store
            self.vector_store = FAISSVectorStore(self.embedding_model)
            self.vector_db = self.vector_store.load_vector_store()

            # 3. Create retriever
            self.retriever = Retriever(self.vector_db)

            # 4. Load LLM
            self.llm = LLMFactory.get_llm()

            # 5. Create response generator
            self.generator = ResponseGenerator(self.llm)

            logger.info("Chat Service initialized successfully")

        except Exception as e:
            raise CustomException(e, sys)

    def ask(self, query: str):
        try:
            logger.info(f"Received query: {query}")

            # Retrieve relevant documents
            docs = self.retriever.retrieve(query)

            # Generate response
            answer = self.generator.generate(query, docs)

            return answer

        except Exception as e:
            raise CustomException(e, sys)
