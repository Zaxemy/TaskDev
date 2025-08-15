from .base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(length=16), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(length=32), unique=True, nullable=True)


