"""
This class will hold common database operations,
essentially linking Pydantic business models with SQLAlchemy models for DB operations
"""
from typing import List, Tuple, Optional

# import sqlalchemy
from fastapi import Query
from pydantic import BaseModel
# from sqlalchemy import text
from sqlalchemy.orm import Session

from common.database.row_models.row_models import PhotographerRow, AddressRow, SubscriptionRow
from common.models.models import Photographer, EventToPhotographer


class Dao:
    @staticmethod
    def paginate_query(query: Query, page: int, size: int) -> Tuple[int, list]:
        paginated_query = query.offset((page - 1) * size).limit(size).all()
        return query.count(), [item for item in paginated_query]

    @staticmethod
    def add_data(data: List[BaseModel], session: Session) -> list:
        """
        Add new items to the database

        Args:
            data: The business models to be put in the database
            session: The database session used to persist the data
        Returns:
            List[ItemRow]: List of inserted items (including new key's, SQLAlchemy takes care of it)
        """
        models = Dao.create_model(photographers=data, session=session)
        session.add_all(models)
        try:
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex

    @staticmethod
    def create_model(photographers: List[BaseModel], session: Session) -> List[PhotographerRow]:
        output = List[PhotographerRow] = []
        for photographer in photographers:
            # todo: Make sure these work with flattened models
            address_row = Dao.get_flat_address(**photographer.address.model_dump(mode="json"))
            # subscription_row = SubscriptionRow(**photographer.subscription.model_dump(mode="json"))
            events = Dao.get_relational_rows(photographer.events, session=session)
            photo_row = PhotographerRow(
                id=photographer.id,
                uid=photographer.uid,
                password=photographer.password,
                first_name=photographer.first_name,
                last_name=photographer.last_name,
                username=photographer.username,
                email=photographer.email,
                avatar=photographer.avatar,
                gender=photographer.gender,
                phone_number=photographer.phone_number,
                social_insurance_number=photographer.social_insurance_number,
                date_of_birth=photographer.date_of_birth,
                address=address_row,
                subscription=subscription_row,
                events=events
            )

            output.append(photo_row)

        return output

    @staticmethod
    def get_relational_rows(event_types: List[EventToPhotographer], session: Session) -> list:
        pass

    @staticmethod
    def get_flat_address(data: dict) -> AddressRow:
        json_dict = {
            "city": data["city"],
            "street_name": data["street_name"],
            "street_address": data["street_address"],
            "state": data["state"],
            "country": data["country"],
            "zip_code": data["zip_code"],

        }
        return AddressRow(**json_dict)

    @staticmethod
    def get_data(session: Session, ids: Optional[list] = None) -> list:
        """
        Retrieve (SELECT) stuff from the DB

        Args:
            session: The database session used to fetch the data
            ids: the ids for the data we need
        Returns:
            list: data for the records we pulled
        """
        photos = []

        if not ids:
            output = session.query(
                PhotographerRow
            )
        else:
            output = session.query(
                PhotographerRow
            ).filter(PhotographerRow.id.in_(ids))

        for rec in output:
            rec_photo = Photographer(**rec.as_dict())
            photos.append(rec_photo)

        return photos

    @staticmethod
    def get_data_by_type(session: Session, type: str) -> list:
        """
        Retrieve (SELECT) stuff from the DB

        Args:
            session: The database session used to fetch the data
            ids: the ids for the data we need
        Returns:
            list: data for the records we pulled
        """
        photos = []

        output = session.query(
            PhotographerRow
        )

        for rec in output:
            if type in rec.event_types:
                rec_photo = Photographer(**rec.as_dict())
                photos.append(rec_photo)

        return photos
