from unittest import TestCase

from common.models.car import Car


class TestModels(TestCase):
    def test_valid_model(self):
        # Confirm that valid JSON data can be parsed into a business model
        data = {
            "key": 1,
            "model": "Tiguan",
            "make": "VW",
            "plate": "ABC-1232",
            "year": "2024-01-01",
            "color": "Grey"
        }

        expected = {
            "key": 1,
            "model": "Tiguan",
            "make": "VW",
            "plate": "ABC-1232",
            "year": "2024-01-01",
            "color": "Grey"
        }

        model = Car(**data)
        assert model.model_dump(mode="json") == expected

    def test_invalid_model(self):
        # Confirm that errors are correctly captured
        data = {
            "model": 1234,
            "make": "VW",
            "plate": "ABC-1232",
            "year": "2024-01-01",
            "color": "Grey"
        }

        with self.assertRaises(Exception):
            model = Car(**data)

