import sys
import traceback
import logging
from networksecurity.logging.logger import logger



def error_message_detail(error, error_details: sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message
""" 
if __name__ == "__main__":
    try:
        logger.info("Divide by zero error")
        a = 1/0
    except Exception as e:
        raise CustomException(e, sys)
"""






