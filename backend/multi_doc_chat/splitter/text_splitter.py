import sys
from typing import List


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

#RecursiveCharacterTextSplitter use cases: Smart splitter that: Tries paragraphs Then sentences
#Then words Then characters

from backend.multi_doc_chat.config.settings import settings
from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException


class TextSplitter:

    def __init__(self):
        self.chunk_size = settings.CHUNK_SIZE 
        self.chunk_overlap = settings.CHUNK_OVERLAP

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:

        try:
            logger.info(
                f"Splitting documents into chunks "
                f"(chunk_size={self.chunk_size}, overlap={self.chunk_overlap})"
            )

            chunks = self.splitter.split_documents(documents)

            logger.info(f"Created {len(chunks)} text chunks")

            return chunks

        except Exception as e:
            raise CustomException(e, sys)

