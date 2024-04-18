from typing import List, Optional

from sqlalchemy.orm import Session

from common.database.row_models.row_models import CarRow
from common.models.car import Car


class Dao:
    @staticmethod
    def save_models(models: List[Car], session: Session) -> Optional[List[int]]:
        rows: List[CarRow] = []

        for model in models:
            # TODO: Define the fail behavior (batch or row). Assuming row here

            # Transform business models into row models
            try:
                row = CarRow(**model.model_dump(mode="json"))
                rows.append(row)
            except Exception as ex:
                # TODO: Create some real logging
                print(f"Could not parse row {model.model_dump(mode='json')}. Error: {str(ex)}")

        try:
            session.add_all(rows)
            session.commit()
            return [row.key for row in rows]
        except Exception as ex:
            # TODO: Create some real logging
            print(f"Could not persist records to DB. Error: {str(ex)}")
            session.rollback()
            return [-1]

