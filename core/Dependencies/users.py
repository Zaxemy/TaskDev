from typing import Annotated, TYPE_CHECKING
from fastapi import Depends, Path, HTTPException
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from core.models.db_helper import db_helper
from core.models.users import User


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.get_db),
    ],
):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)
