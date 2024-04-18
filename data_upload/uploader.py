from csv import DictReader
from typing import List

from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.models.car import Car


class Uploader:
    def __init__(self, session: Session):
        self.valid_data: List[Car] = []
        self.invalid_data = {}
        self.session = session

    def upload(self, filename: str) -> List[int]:
        # Asume that this is the only folder for upload files
        # TODO: make this more flexible
        filename = f"./uploads/{filename}"
        with open(filename, "r") as file:
            reader = DictReader(file)
            # TODO: Confirm if we should fail files completely or by row. Assuming by row
            for i, rec in enumerate(reader):
                try:
                    model = Car(**rec)
                    self.valid_data.append(model)
                except Exception as ex:
                    # TODO: Replace with real logging
                    print(f"Error parsing row {i}: {str(ex)}")
                    self.invalid_data[i] = model

        return self.save_to_db()

    def save_to_db(self) -> List[int]:
        # Easy version:
        # return Dao.save_models(self.valid_data)

        # Batching
        # TODO: We can improve this depending on if we want to fail at the file level
        output: List[int] = []
        i = 0
        size = 100
        end = i + size
        batch = self.valid_data[i:end]
        while batch:
            output.extend(Dao.save_models(batch,session=self.session))
            i = end
            end = i + size
            batch = self.valid_data[i:end]

        return output
