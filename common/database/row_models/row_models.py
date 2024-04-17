from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from common.database.database import Base


class PatientRow(Base):
    __tablename__ = "tblPatient"

    key: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    ssn: Mapped[str] = mapped_column()
    height: Mapped[Decimal] = mapped_column()
    weight: Mapped[Decimal] = mapped_column()
    name: Mapped[str] = mapped_column()
    admitted: Mapped[str] = mapped_column()
    birthday: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    occupation: Mapped[str] = mapped_column()