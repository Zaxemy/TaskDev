from core.Dependencies.access_tokens import get_access_token_db
from core.config import settings
from typing import TYPE_CHECKING
from fastapi import Depends
from fastapi_users.authentication.strategy.db import (
    DatabaseStrategy,
)
from typing import Annotated

if TYPE_CHECKING:
    from core.models.access_token import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_token_db),
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        access_token_db, lifetime_seconds=settings.access_token.lifetime_seconds
    )
