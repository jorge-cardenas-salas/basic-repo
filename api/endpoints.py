from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.database.database import get_session
from common.models.car import Car
from data_upload.uploader import Uploader

app = FastAPI()


@app.get("/is-alive")
def is_alive() -> bool:
    return True


@app.put("/add-records")
def add_records(models: List[Car], session: Session = Depends(get_session)):
    return Dao.save_models(models, session=session)


@app.put("/upload-file")
def upload_file(filename: str, session: Session = Depends(get_session)):
    try:
        uploader = Uploader(session=session)
        return uploader.upload(filename)
    except Exception as ex:
        print(f"Ooopsie! : {str(ex)}")
        return [-1]
