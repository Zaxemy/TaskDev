from fastapi_users.authentication import  JWTStrategy
from core.config import settings


def get_jwt_strategy() -> JWTStrategy:
    """
    Стратегия JWT
    """
    return JWTStrategy(
        secret=settings.jwt_auth.SECRET,
        lifetime_seconds=settings.jwt_auth.LIFETIME_SECONDS,
        algorithm=settings.jwt_auth.ALGORITHM,
    )
