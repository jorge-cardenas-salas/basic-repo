"""
Unit test cases for Pydantic models and associated logic go here
"""
from unittest import TestCase

from common.models.models import Subscription, Photographer


# from common.models.item_model import Item


class TestModels(TestCase):
    def test_valid_data(self):
        """
        Parse valid data as a model and assess results
        """
        data = {
            "plan": "Essential",
            "status": "Blocked",
            "payment_method": "Alipay",
            "term": "Monthly"
        }

        model = Subscription(**data)

        expected = {
            "plan": "Essential",
            "status": "Blocked",
            "payment_method": "Alipay",
            "term": "Monthly"
        }
        self.assertEqual(
            expected,
            model.model_dump(mode="json")
        )

    def test_invalid_data(self):
        """
        Parse invalid data and make sure an error is raised
        Returns:

        """
        data = {
            "plan": 1234,
            "status": "Blocked",
            "payment_method": "Alipay",
            "term": "Monthly"
        }
        with self.assertRaises(Exception):
            # Parse model here
            model = Subscription(**data)

    def test_whole_thing(self):
        data = {
            "id": 4072,
            "uid": "c7204a53-77be-4ba6-b446-8f92921060a0",
            "password": "uDQXExV6pr",
            "first_name": "Lorenzo",
            "last_name": "Fay",
            "username": "lorenzo.fay",
            "email": "lorenzo.fay@email.com",
            "avatar": "https://robohash.org/autconsecteturlabore.png?size=300x300&set=set1",
            "gender": "Polygender",
            "phone_number": "+503 758-280-5371 x9138",
            "social_insurance_number": "770448660",
            "date_of_birth": "1993-01-18",
            "event_type": {
                "type": ["wedding", "bridal showers", "food", "sports"]
            },
            "address": {
                "city": "Noemouth",
                "street_name": "Eusebio Point",
                "street_address": "4999 Alfredia Station",
                "zip_code": "71586",
                "state": "Arizona",
                "country": "United States",
                "coordinates": {
                    "lat": -63.81164074947457,
                    "lng": 119.54873167874729
                }
            },
            "credit_card": {
                "cc_number": "4425-3666-4612-3889"
            },
            "subscription": {
                "plan": "Platinum",
                "status": "Blocked",
                "payment_method": "Alipay",
                "term": "Full subscription"
            }
        }
        model = Photographer(**data)

        expected = {
            "id": 4072,
            "uid": "c7204a53-77be-4ba6-b446-8f92921060a0",
            "password": "uDQXExV6pr",
            "first_name": "Lorenzo",
            "last_name": "Fay",
            "username": "lorenzo.fay",
            "email": "lorenzo.fay@email.com",
            "avatar": "https://robohash.org/autconsecteturlabore.png?size=300x300&set=set1",
            "gender": "Polygender",
            "phone_number": "+503 758-280-5371 x9138",
            "social_insurance_number": "770448660",
            "date_of_birth": "1993-01-18",
            "event_type": {
                "type": ["wedding", "bridal showers", "food", "sports"]
            },
            "address": {
                "city": "Noemouth",
                "street_name": "Eusebio Point",
                "street_address": "4999 Alfredia Station",
                "zip_code": "71586",
                "state": "Arizona",
                "country": "United States",
                "lat": -63.81164074947457,
                "lng": 119.54873167874729
            },
            "credit_card_number": "4425-3666-4612-3889",
            "subscription": {
                "plan": "Platinum",
                "status": "Blocked",
                "payment_method": "Alipay",
                "term": "Full subscription"
            }
        }

        self.assertEqual(
            expected,
            model.model_dump(mode="json")
        )
