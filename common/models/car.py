import datetime
from typing import Optional

from pydantic import BaseModel


class Car(BaseModel):
    key: Optional[int] = None
    model: str
    make: str
    plate: str
    year: datetime.date
    color: str

    class Config:
        # Allows ORM for this model
        from_attributes = True
