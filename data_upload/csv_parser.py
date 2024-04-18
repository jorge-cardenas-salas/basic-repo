"""
Class to upload files into the database
"""

# import csv
# import json
# from csv import DictReader
from logging import Logger
from typing import Optional, List

from click.core import batch
from pydantic import BaseModel  # , ValidationError
from sqlalchemy.orm import Session, sessionmaker

# from common.database.daos.dao import Dao
# from common.models.item_model import Item
from common.constants import UploadFailMode
from common.database.database import engine
from common.utilities import DefaultLogger


class CsvParser:
    EXPECTED_HEADERS = {"name"}

    def __init__(
            self,
            session: Session,
            logger: Optional[Logger] = None,
            fail_mode: UploadFailMode = UploadFailMode.BATCH
    ):
        # Valid/Invalid data will be dicts, using the row number as a key, for reference
        self.invalid_data: dict = {}
        self.valid_data: dict = {}
        self.logger: Logger = logger or DefaultLogger().get_logger()

        # Fail mode: if a single item in a batch fails, should we commit or fail the whole batch?
        self.fail_mode: UploadFailMode = fail_mode
        self.success = True
        self.filename: str = ""
        self.session: Session = session

    def upload(self, filename: str) -> bool:
        """
        Upload the selected file to the system (database)

        Args:
            filename: The file to upload
        Returns:
            bool: True if all records were successful, false otherwise
        """
        raise NotImplementedError()

    def write_error_report(self):
        """
        Write an error report for failures
        """
        raise NotImplementedError()

    def add_to_db(self, models: List[BaseModel], i: Optional[int] = None):
        """
        Persist the models to the database
        Args:
            models: The models to be inserted
            i: The row number from the CSV (only for fail_mode == ROW)
        """
        parts = batch(models, batch_size=100)
        for part in parts:
            self.session.add_all(part)

    def parse_row(self, i: int, row: dict):
        """
        Parse a single CSV row and add it to the valid data (if applicable)

        Args:
            i: The CSV row number for reference
            row: A dict representation of a CSV row
        """
        raise NotImplementedError()


if __name__ == "__main__":
    # Generate a DB session
    TestSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    with TestSessionLocal() as session:
        parser = CsvParser(session=session, fail_mode=UploadFailMode.BATCH)
        parser.upload("../tests/data/validData.csv")
