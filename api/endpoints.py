from typing import List

from fastapi import Depends, FastAPI  # , HTTPException, status
from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
# from common.database.daos.dao import Dao
from common.database.database import get_session
from common.models.models import Photographer
# from data_upload.csv_parser import CsvParser
from common.utilities import DefaultLogger
from data_upload.json_parser import JsonParser

app = FastAPI()

logger = DefaultLogger().get_logger()


@app.get("/is-alive")
def is_alive() -> dict:
    return {"alive": True}


@app.put("/add-file")
def add_file(filename, session: Session = Depends(get_session)):
    try:
        uploader = JsonParser()
        uploader.upload(filename, session=session)
    except Exception as ex:
        logger.exception(f"Error uploading file: {str(ex)}")


@app.get("/get-all")
def get_all(session: Session = Depends(get_session)) -> List[Photographer]:
    # TODO: This method could be merged with the one below
    try:
        return Dao.get_data(ids=None, session=session)
    except Exception as ex:
        logger.exception(f"Error getting data: {str(ex)}")


@app.get("/get-some")
def get_all(ids=List[int], session: Session = Depends(get_session)) -> List[Photographer]:
    try:
        return Dao.get_data(ids=ids, session=session)
    except Exception as ex:
        logger.exception(f"Error getting data: {str(ex)}")


@app.get("/get-by-type")
def get_all(type=str, session: Session = Depends(get_session)) -> List[Photographer]:
    try:
        return Dao.get_data_by_type(type=str, session=session)
    except Exception as ex:
        logger.exception(f"Error getting data: {str(ex)}")
