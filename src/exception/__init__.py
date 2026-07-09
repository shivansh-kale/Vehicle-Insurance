import sys          # Used to get exception traceback information
import logging      # Used to log error messages

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log the error for better tracking
    logging.error(error_message)
    
    return error_message


# Create a custom exception class
class MyException(Exception):
    """
    Custom exception class for handling errors in the US visa application.
    """
    def __init__(self, error_message: str, error_detail: sys):         #Runs automatically when the exception object is created.
        """
        Initializes the USvisaException with a detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback details.
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:                  # it allows detailed error msg , rather thsn just print(e)--> Myexception
        """
        Returns the string representation of the error message.
        """
        return self.error_message