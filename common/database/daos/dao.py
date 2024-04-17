from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from common.database.row_models.row_models import PatientRow


class Dao:

    @staticmethod
    def add_data(models: List[BaseModel], session: Session) -> Optional[List[PatientRow]]:
        # Assume row-level (not batch) failure
        rows = []
        for model in models:
            try:
                row = PatientRow(**model.model_dump(mode="json"))
                rows.append(row)
            except Exception as ex:
                print(f"Failure parsing model \n{model.model_dump(mode='json')}\nto patient row:\n{str(ex)}")

        # Now try to add them all at once
        try:
            session.add_all(rows)
            session.commit()
            return rows
        except Exception as ex:
            print(f"Error persisting rows to DB: {str(ex)}")
            session.rollback()
            return None