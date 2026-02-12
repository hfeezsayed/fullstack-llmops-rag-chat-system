import os
import sys

from typing import List

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


from backend.multi_doc_chat.config.settings import settings
from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException


class FAISSVectorStore:

    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.index_path = settings.VECTOR_DB_PATH

    #create vector store
    def create_vector_store(self, documents: List[Document]):

        try:
            logger.info("Creating FAISS vector store")
            vectorstore = FAISS.from_documents(#FAISS.from_documents - it creates searchable memory.
                documents,
                self.embeddings
            )
            return vectorstore
        except Exception as e:
            raise CustomException(e, sys)
        
    #save vector store
    def save_vector_store(self, vectorstore):

        try:
            logger.info(f"Saving FAISS index at {self.index_path}")
            os.makedirs(self.index_path, exist_ok=True)
            vectorstore.save_local(self.index_path)
            #save_local(): Stores index on disk, So system does NOT need to rebuild embeddings every time.

        except Exception as e:
            raise CustomException(e, sys)
        
    #load vector store
    def load_vector_store(self):

        try:
            logger.info("Loading FAISS vector store")
            vectorstore = FAISS.load_local(#FAISS.load_local: Loads saved vector DB instantly.
                self.index_path,
                self.embeddings,
                allow_dangerous_deserialization=True #Required in latest LangChain FAISS loading.

            )
            return vectorstore
        
        except Exception as e:
            raise CustomException(e, sys)

