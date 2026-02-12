import sys
from typing import List #List: Used to return multiple documents.

from langchain_core.documents import Document #LangChain standard document object and Retriever always returns list of Document.
from backend.multi_doc_chat.logger.logging import logger #logger: For production monitoring.
from backend.multi_doc_chat.exceptions.custom_exception import CustomException #CustomException: For clean debugging.


class Retriever:

    def __init__(self, vectorstore, k: int = 3):
        self.vectorstore = vectorstore #Already created FAISS database so Retriever uses it to search.
        self.k = k #k is Top number of documents to return. ex: k = 3 → Return top 3 relevant chunks
    
    def retrieve(self, query: str) -> List[Document]:
        try:
            logger.info("Retrieving relevant documents")

            retriever = self.vectorstore.as_retriever(#Converts FAISS into searchable engine.
                search_kwargs={"k": self.k} #How many best matches return
            )

            documents = retriever.invoke(query) #Query → Embedding → Similarity Search → Return Documents

            return documents

        except Exception as e:
            raise CustomException(e, sys)

 
