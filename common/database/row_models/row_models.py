from sqlalchemy.orm import Mapped, mapped_column

from common.database.database import Base


class CarRow(Base):
    __tablename__ = "tblCar"

    key: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column()
    make: Mapped[str] = mapped_column()
    plate: Mapped[str] = mapped_column()
    year: Mapped[str] = mapped_column()
    color: Mapped[str] = mapped_column()
