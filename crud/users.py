from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas import users as schemas
from core.models.users import User
from sqlalchemy import select
from core.models import users as models
from utils.jwt_auth import get_password_hash
from utils.jwt_auth import get_password_hash

async def get_user_by_username(session: AsyncSession, username: str) -> models.User | None:
    """
    Получает пользователя из БД по имени.
    Возвращает объект User или None, если пользователь не найден.
    """
    query = select(models.User).where(models.User.username == username)
    result = await session.execute(query)
    
    return result.scalar_one_or_none()


async def create_user(session: AsyncSession, user: schemas.UserCreate) -> models.User:
    """Создает нового пользователя в БД."""
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user