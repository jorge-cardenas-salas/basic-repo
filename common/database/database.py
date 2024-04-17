from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from common.constants import PROJECT_NAME

CONN_STR = f"sqlite:////app/resources/{PROJECT_NAME}.db"

engine = create_engine(CONN_STR)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    except Exception as ex:
        session.close()
