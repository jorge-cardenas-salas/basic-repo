from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.database.database import get_session
from common.models.patient import Patient
from data_upload.uploader import Uploader

app = FastAPI()


@app.get("/is-alive")
def is_alive() -> dict:
    return {"alive": True}


@app.put("/create-models")
def create_models(models: List[Patient], session: Session = Depends(get_session)) -> List[int]:
    try:
        rows = Dao.add_data(models=models, session=session)
        return [row.key for row in rows]
    except Exception as ex:
        print(f"Ooopsie!!: {str(ex)}")
        return [-1]


@app.put("/upload-file")
def upload_file(filename: str, session: Session = Depends(get_session)) -> List[int]:
    uploader = Uploader(session=session)
    return uploader.upload(filename)
