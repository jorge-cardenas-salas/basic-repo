from typing import List
from unittest import TestCase
from unittest.mock import patch, Mock

from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.database.row_models.row_models import ItemRow
# from data_upload.csv_parser import CsvParser


def mock_dao_return_values() -> List[ItemRow]:
    return [
        ItemRow(key=1),
        ItemRow(key=2),
    ]


class TestDataUpload(TestCase):
    @patch.object(Dao, "add_data", return_value=mock_dao_return_values())
    @patch.object(Session, "close", return_value=None)
    def test_invalid_data(self, *args):
        self.assertEqual(1, 1)
        # TODO implement test
        # with self.assertLogs() as check_log:
        #     mock_session = Mock()
        #     parser = CsvParser(session=mock_session)
        #     result = parser.upload("/app/tests/data/invalidData.csv")
        #     self.assertFalse(result)
        #     log_text = str(check_log.output)
        #     self.assertIn("Value doesn\\'t match expected pattern", log_text)
