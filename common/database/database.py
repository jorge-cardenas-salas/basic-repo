from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from common.constants import PROJECT_NAME

CONN_STRING = f"sqlite:////app/resources/{PROJECT_NAME}.db"

engine = create_engine(CONN_STRING)

SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.close()
