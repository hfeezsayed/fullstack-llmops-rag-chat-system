import os
import sys

from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
#Directory Loader: Loads multiple files automatically from folder.

from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException



class DocumentLoader:

    def __init__(self, data_path: str):
        self.data_path = data_path


    def load_documents(self):

        try:
            logger.info(f"Loading documents from: {self.data_path}")

            txt_loader = DirectoryLoader(
                self.data_path,
                glob="*.txt", #Tells loader to only pick .txt files.
                loader_cls=TextLoader
                # loader_cls: Specifies how to parse file type. TXT → TextLoader
            )

            pdf_loader = DirectoryLoader(
                self.data_path,
                glob="*.pdf", ##Tells loader to only pick .pdf files.
                loader_cls=PyPDFLoader
                # loader_cls: Specifies how to parse file type. PDF → PyPDFLoader
            )

            txt_documents = txt_loader.load()
            pdf_documents = pdf_loader.load()


            documents = txt_documents + pdf_documents
            #Combines all documents into one list.

            logger.info(f"Loaded {len(documents)} documents successfully")

            return documents
        
        except Exception as e:
            raise CustomException(e, sys) #CustomException: Captures file + line number if failure happens.