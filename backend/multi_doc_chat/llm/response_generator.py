from langchain_core.prompts import ChatPromptTemplate
from backend.multi_doc_chat.logger.logging import logger
from backend.multi_doc_chat.exceptions.custom_exception import CustomException
import sys


class ResponseGenerator:

    def __init__(self, llm):
        self.llm = llm

    def generate(self, query: str, documents):
        try:
            logger.info("Generating response from LLM")

            context = "\n\n".join([doc.page_content for doc in documents])

            prompt = ChatPromptTemplate.from_template(
                """
                Answer the question based only on the context below.

                Context:
                {context}

                Question:
                {question}
                """
            )

            chain = prompt | self.llm

            response = chain.invoke({
                "context": context,
                "question": query
            })

            return response.content

        except Exception as e:
            raise CustomException(e, sys)
