from csv import DictReader
from typing import List

from sqlalchemy.orm import Session

from common.database.daos.dao import Dao
from common.models.patient import Patient


class Uploader:
    def __init__(self, session: Session):
        self.valid_data = []
        self.invalid_data = {}
        self.session = session

    def upload(self, filename: str) -> List[int]:
        # Assume file in the uploads folder
        filename = f"./uploads/{filename}"

        # TODO: Clean this code, it is too nested
        try:
            with open(filename, "r") as file:
                reader = DictReader(file)
                for i, row in enumerate(reader):
                    # TODO: Decide weather to fail by row or by file. This method assumes row
                    try:
                        model = Patient(**row)
                        self.valid_data.append(model)
                    except Exception as ex:
                        # TODO: Add real logging here
                        print(f"Error parsing row {i}: {row}\n {str(ex)}")
                        self.invalid_data[i] = row
            return self.save_data()
        except Exception as ex:
            print(f"Generic error processing file: {str(ex)}")
            return [-1]

    def save_data(self) -> List[int]:
        # Batch save
        # TODO: Batching can be cleaner and more flexible
        output = []
        i = 0
        size = 100  # TODO This should be configurable
        end = i + size
        batch = self.valid_data[i:end]
        while batch:
            # TODO: DAO takes care of err handling, but we should know if we should fail all at once
            results = Dao.add_data(batch,session=self.session)
            if not results:
                print(f"Error saving batch")
            else:
                output.extend([result.key for result in results])

            i = end
            end = i + size
            batch = self.valid_data[i:end]

        return output
