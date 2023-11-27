import os.path
import sys
import yaml
import base64

from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


def read_yaml_file(file_path: str) -> dict:
    '''
    Read yaml file
    '''
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e
    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    '''
    Create yaml file
    '''
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)
    


def decodeImage(imgstring, fileName):
    """
    Decodes a base64-encoded image string and saves it to a file.

    Parameters:
    - imgstring (str): A base64-encoded image string to be decoded.
    - fileName (str): The name of the file to be created to store the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    Encodes an image from a specified file path into a base64-encoded string.

    Parameters:
    - croppedImagePath (str): The path to the image file to be encoded.

    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
