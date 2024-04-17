"""
Model representation of an element within our system

We leverage pydantic as it makes it easier to write, validate and manage relationships for data
"""
# import re
# from typing import Optional, List

from pydantic import BaseModel, field_validator  # , Field, PastDate, EmailStr


class Item(BaseModel):
    # Properties
    key: int

    @field_validator("name")
    @classmethod
    def validate_field(cls, value: str) -> str:
        """
        Sample validation
        Args:
            value: The value to be evaluated
        Returns:
            str: The same value, assuming validation passed
        """
        raise NotImplementedError()

    class Config:
        """
        Pydantic-specific config, specifically from_attributes tells pydantic this is part of an Object-Relational mapping
        """
        from_attributes = True
