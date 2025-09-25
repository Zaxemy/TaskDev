from fastapi_users import FastAPIUsers

from core.models.users import User
from core.authentication.auth_backend import auth_backend
from core.authentication.manage_auth import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)