"""
Table row models will live here.

These will be tied to the overall declarative base and to one-another.

Note that we are NOT implementing any queries here, that happens in the DAO
"""
# from typing import List, Optional
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column  # , relationship

from common.database.database import Base


class ItemRow(Base):
    """
    Class representation of a DB table row

    Note how we sub-class from Base, this is to allow SQL Alchemy to tie all models together
    """
    __tablename__ = "TBD"

    # Here we create field values and associate them to DB columns
    key: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self) -> dict:
        """
        Handy method to serialize my class as a dictionary

        Returns:
            dict representation of this class
        """
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

