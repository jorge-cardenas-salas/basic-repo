"""
Unit test cases for Pydantic models and associated logic go here
"""
from unittest import TestCase


# from common.models.item_model import Item


class TestModels(TestCase):
    def test_valid_data(self):
        """
        Parse valid data as a model and assess results
        """
        data = {}

        self.assertEqual(
            data,
            {}
        )

    def test_invalid_data(self):
        """
        Parse invalid data and make sure an error is raised
        Returns:

        """
        data = {
            "key": 1
        }
        with self.assertRaises(Exception):
            # Parse model here
            result = 1 / 0
