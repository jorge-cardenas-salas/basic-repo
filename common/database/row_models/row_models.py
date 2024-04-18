"""
Table row models will live here.

These will be tied to the overall declarative base and to one-another.

Note that we are NOT implementing any queries here, that happens in the DAO
"""
from decimal import Decimal
from typing import List

# from typing import List, Optional
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship  # , relationship

from common.database.database import Base


class EventToPhotographerRow(Base):
    __tablename__ = "tblEventToPhotographer"

    type: Mapped[str] = mapped_column(primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

class EventTypeRow(Base):
    __tablename__ = "tblEventType"

    type: Mapped[str] = mapped_column(primary_key=True)


class SubscriptionRow(Base):
    __tablename__ = "tblSubscription"

    id: Mapped[int] = mapped_column(primary_key=True)
    photographer_id: Mapped[int] = mapped_column()
    plan: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    payment_method: Mapped[str] = mapped_column()
    term: Mapped[str] = mapped_column()


class AddressRow(Base):
    __tablename__ = "tblAddress"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column()
    street_name: Mapped[str] = mapped_column()
    street_address: Mapped[str] = mapped_column()
    zip_code: Mapped[str] = mapped_column()
    state: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    lat: Mapped[Decimal] = mapped_column()
    lng: Mapped[Decimal] = mapped_column()


class PhotographerRow(Base):
    __tablename__ = "tblPhotographer"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    avatar: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    social_insurance_number: Mapped[str] = mapped_column()
    date_of_birth: Mapped[str] = mapped_column()
    address: Mapped["AddressRow"] = relationship()
    subscription: Mapped["SubscriptionRow"] = relationship()
    event_types: Mapped[List["EventTypeRow"]] = relationship()

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in
               ["password", "social_insurance_number", "address", "subscription", "event_types"]
        }
