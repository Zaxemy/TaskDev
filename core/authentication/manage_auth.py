from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from core.models.users import User
from core.config import settings
import logging


logger = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.jwt_auth.SECRET
    verification_token_secret = settings.jwt_auth.SECRET

    async def on_after_register(self, user: User, request: Request | None = None):
        logger.info(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Request | None = None
    ):
        logger.info(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Request | None = None
    ):
        logger.info(
            f"Verification requested for user {user.id}. Verification token: {token}"
        )


async def get_user_manager(user_db):
    """Получение User_Manager"""
    yield UserManager(user_db)
