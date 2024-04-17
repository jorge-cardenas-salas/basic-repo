from typing import Optional

from pydantic import BaseModel, PastDate


class Patient(BaseModel):
    key: Optional[int] = None
    ssn: str
    height: float
    weight: float
    name: str
    admitted: PastDate
    birthday: PastDate
    phone: str
    email: str
    gender: str
    occupation: str

    class Config:
        """
        This one is needed to allow ORM with pydantic
        """
        from_attributes = True
