from fastapi_users import schemas
from pydantic import BaseModel, EmailStr, Field


class UserRead(schemas.BaseUser):
    """
    Схема для чтения данных пользователя
    """

    id: int
    username: str
    email: EmailStr
    first_name: str | None
    last_name: str | None


class UserCreate(schemas.BaseUserCreate):
    """
    Схема для создания пользователя
    """

    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class UserUpdate(schemas.BaseUserUpdate):
    """
    Схема для обновления пользователя
    """

    username: str | None = None
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None
