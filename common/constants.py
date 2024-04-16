"""
Project constants
"""
import os
from enum import Enum

from dotenv import load_dotenv

# We will use .env for configuration
load_dotenv()

PROJECT_NAME = os.getenv('PROJECT_NAME')

# Format to be used by the logger
DEFAULT_LOG_FORMAT = "%(asctime)s | %(levelname)s | %(module)s.%(processName)s: %(message)s"

# DB Connectivity parameters
DB_CONN = {
    "server": os.getenv("DB_SERVER"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "pwd": os.getenv("DB_PWD"),
    "name": os.getenv("DB_NAME"),
}


class UploadFailMode(Enum):
    BATCH = 0
    ROW = 1
