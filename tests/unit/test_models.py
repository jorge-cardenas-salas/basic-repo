from unittest import TestCase

from common.models.patient import Patient


class TestModels(TestCase):
    def test_valid_data(self):
        data = {
            "ssn": "555-555-55",
            "height": 107.0,
            "weight": 80,
            "name": "Jorge Cardenas",
            "admitted": "2024-04-11",
            "birthday": "1977-02-21",
            "phone": "555-555-5555",
            "email": "jorge@me.com",
            "gender": "Male",
            "occupation": "SW Engineer"
        }
        expected = {
            "key": None,
            "ssn": "555-555-55",
            "height": 107.0,
            "weight": 80,
            "name": "Jorge Cardenas",
            "admitted": "2024-04-11",
            "birthday": "1977-02-21",
            "phone": "555-555-5555",
            "email": "jorge@me.com",
            "gender": "Male",
            "occupation": "SW Engineer"
        }

        model = Patient(**data)
        actual = model.model_dump(mode="json")

        assert expected == actual

    def test_invalid_data(self):
        data = {
            "ssn": "555-555-55",
            "height": 107.0,
            "weight": "eighty",
            "name": "Jorge Cardenas",
            "admitted": "2024-04-11",
            "birthday": "1977-02-21",
            "phone": "555-555-5555",
            "email": "jorge@me.com",
            "gender": "Male",
            "occupation": "SW Engineer"
        }

        with self.assertRaises(Exception):
            model = Patient(**data)

