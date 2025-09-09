from typing import Annotated, TYPE_CHECKING
from fastapi import Depends, Path, HTTPException
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from core.models.db_helper import db_helper
from core.models.users import User
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from core.models.access_token import AccessToken
if TYPE_CHECKING:
    from core.models.access_token import AsyncSession


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.get_db),
    ],
):

    yield AccessToken.get_db(session=session)
