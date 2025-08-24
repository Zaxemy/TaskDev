from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.models.db_helper import db_helper
from crud import users as crud_user
from fastapi import status
from utils import jwt_auth as security
from core.schemas import users as schemas
from sqlalchemy import select
from core.models import users as models
from core.Dependencies.auth import get_current_user


router = APIRouter(prefix="/users")


@router.post("/register/", response_model=schemas.User)
async def register_user(
    user: schemas.UserCreate, session: AsyncSession = Depends(db_helper.get_db)
):
    """Регистрирует нового пользователя."""

    db_user = await crud_user.get_user_by_username(
        session=session, username=user.username
    )

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    return await crud_user.create_user(session=session, user=user)


@router.post("/token/", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(db_helper.get_db),
):
    """Аутентифицирует пользователя и возвращает токен."""
    user = await crud_user.get_user_by_username(session, username=form_data.username)
    if not user or not security.verify_password(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    """Возвращает данные текущего авторизованного пользователя."""
    return current_user
