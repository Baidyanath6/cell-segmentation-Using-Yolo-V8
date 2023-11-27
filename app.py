import sys
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException


logging.info("welcome to the custom log")

try:
    a = '2'/4

except Exception as e:
    raise AppException(e, sys)
