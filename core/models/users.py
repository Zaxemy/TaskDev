from .base import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer
from typing import TYPE_CHECKING

from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTable[UserIdType], Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session=session, user_table=cls)
