import json

from sqlalchemy.orm import Session

from common.database.daos.dao import Dao


class JsonParser:
    def upload(self,filename,session:Session):
        filename = f"./uploads/{filename}"
        with open(filename,"r") as file:
            data = json.load(file)
            Dao.add_data(data=data, session=session)
