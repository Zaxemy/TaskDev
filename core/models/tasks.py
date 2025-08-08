from base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Task(Base):
    title: Mapped[str] = mapped_column(String(64), unique=True)
    description: Mapped[str] = mapped_column(String(256))
    is_complete: Mapped[bool] = mapped_column(default=False)

