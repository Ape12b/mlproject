import sys

class CustomException(Exception):
    def __init__(self, message, error_detail:sys):
        self.message = message
        super().__init__(message)
        self.print_exception_info(message, error_detail)

    def print_exception_info(self, message, error_detail):
        # Print custom exception details
        exc_type, exc_obj, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        lineno = exc_tb.tb_lineno
        exception_type = exc_type.__name__
        self.error_message = f"\nCustom Exception: [{message}] in File: [{filename}] at Location: Line [{lineno}]\nException Type: [{exception_type}]"
    
    def __str__(self):
        return self.error_message

    
    