import sys
from backend.multi_doc_chat.logger.logging import logger

#this file use case: Every will pass throgh this.
class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        self.error_message = self.get_detailed_error_message(
            error_message,
            error_detail
        )

    def get_detailed_error_message(self, error_message, error_detail: sys):

        _, _, exc_tb = error_detail.exc_info()#this will captures: filename, line number and Error Traceback

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        detailed_error = (
            f"Error occurred in script: {file_name} "
            f"at line: {line_number} "
            f"with message: {error_message}"
        )

        logger.error(detailed_error)#Logs error automatically to log file.

        return detailed_error

    def __str__(self): #Controls how error prints.
        return self.error_message
