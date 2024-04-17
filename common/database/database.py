"""
In this class we will create common database elements

Using SQLAlchemy for ORM management as it makes DB handling seamless regardless of SQL dialect
"""
import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from common.constants import PROJECT_NAME, DB_CONN

USE_SQLITE = True


def sqlite_str():
    """
    Get the connection string for local sqlite database. Good for lightweight and reliability
    Returns:
        str: A connection string tied to this specific project
    """
    # Absolute, for non-Docker testing
    # return f"sqlite:///C:/Users/Jorge/Projects/{PROJECT_NAME}/resources/{PROJECT_NAME}.db"
    # For Docker-testing only:
    return f"sqlite:////app/resources/{PROJECT_NAME}.db"


# Get DB engine
engine = create_engine(sqlite_str())

# Now, create the session generator, make sure we don't automatically flush or commit for the main session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# This ties all our DB models together in SQLAlchemy
Base = declarative_base()


def get_session() -> SessionLocal:
    """
    Retrieve an individual session to be used for our queries, then close it when done.
    This approach also works great with SQLAlchemy dependencies for testing

    Returns:
        SessionLocal: the session to be used
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
