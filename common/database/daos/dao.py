"""
This class will hold common database operations,
essentially linking Pydantic business models with SQLAlchemy models for DB operations
"""
from typing import List, Tuple

# import sqlalchemy
from fastapi import Query
from pydantic import BaseModel
# from sqlalchemy import text
from sqlalchemy.orm import Session

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
        raise NotImplementedError()

    @staticmethod
    def get_data(ids: list, session: Session) -> list:
        """
        Retrieve (SELECT) stuff from the DB

        Args:
            session: The database session used to fetch the data
            ids: the ids for the data we need
        Returns:
            list: data for the records we pulled
        """
        raise NotImplementedError()

    @staticmethod
    def delete_items(session: Session, ids: List[int]) -> bool:
        """
        Delete stuff from our DB
        Args:
            session: The database session used to fetch the data
            ids: the ids for the data we need
        Returns:
            bool: True if success, False otherwise
        """
        raise NotImplementedError()

    @staticmethod
    def update_item(key: int, model: BaseModel, session: Session) -> bool:
        """
        Update data

        Args:
            session: The database session used to fetch the data
            model: The model data we will update
            key: the specific record to be updated
        Returns:
            bool: True if success, False otherwise
        """
        raise NotImplementedError()

    @staticmethod
    def raw_sql_placeholder(data: dict, session: Session) -> bool:
        """
        Allow SQL execution

        Args:
            data: The data to be used in our SQL
            session: The database session used to fetch the data
        Returns:
            bool: True if success, False otherwise
        """
        raise NotImplementedError()
