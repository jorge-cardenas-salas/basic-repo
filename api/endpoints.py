from typing import List

from fastapi import Depends, FastAPI  # , HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

# from common.database.daos.dao import Dao
from common.database.database import get_session
# from data_upload.csv_parser import CsvParser
from common.utilities import DefaultLogger

app = FastAPI()

logger = DefaultLogger().get_logger()


@app.get("/is-alive")
def is_alive() -> dict:
    return {"alive": True}


@app.put("/add-data")
def add_items(models: List[BaseModel], session: Session = Depends(get_session)) -> List[int]:
    """
    Endpoint to add new things to our database
    
    Args:
        models: One or more models to be added 
        session: The SQLAlchemy session we'll use for the DB 
    Returns:
        list of newly created key's
    """
    raise NotImplementedError()


@app.post("/get-data")
def retrieve_items(ids: List[int], session: Session = Depends(get_session)):
    raise NotImplementedError()
