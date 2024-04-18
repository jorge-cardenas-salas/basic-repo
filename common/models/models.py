"""
Model representation of an element within our system

We leverage pydantic as it makes it easier to write, validate and manage relationships for data
"""
from decimal import Decimal
from typing import List

from pydantic import BaseModel, PastDate, root_validator , model_validator # , Field, PastDate, EmailStr


class EventToPhotographer(BaseModel):
    type: str
    id: int


class EventType(BaseModel):
    type: str


class Subscription(BaseModel):
    plan: str
    status: str
    payment_method: str
    term: str

    class Config:
        """
        Pydantic-specific config, specifically from_attributes tells pydantic this is part of an Object-Relational mapping
        """
        from_attributes = True


class Address(BaseModel):
    city: str
    street_name: str
    street_address: str
    zip_code: str
    state: str
    country: str
    lat: Decimal
    lng: Decimal


class Photographer(BaseModel):
    id: int
    uid: str
    password: str
    first_name: str
    last_name: str
    username: str
    email: str
    avatar: str
    gender: str
    phone_number: str
    social_insurance_number: str
    date_of_birth: PastDate
    credit_card_number: str
    address: Address
    subscription: Subscription
    events: List[EventToPhotographer]

    class Config:
        """
        Pydantic-specific config, specifically from_attributes tells pydantic this is part of an Object-Relational mapping
        """
        from_attributes = True
