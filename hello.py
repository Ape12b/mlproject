from src.exception import CustomException
import sys
try:
    print(10/0)
except Exception as ce:
        # The exception details will be printed automatically
        raise CustomException(ce,  sys)