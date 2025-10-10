from pydantic_settings import BaseSettings
from pydantic import BaseModel


class DataBaseSettings(BaseModel):
    db_url: str = "postgresql+asyncpg://postgres:12345@db:5432/taskdev"
    echo: bool = True


class JWTAuth(BaseModel):
    SECRET: str = "993Nqs9GkGgF7NwDmJc3xE2wI6S1De3XPreg70SXu-E"

    ALGORITHM: str = "HS256"
    LIFETIME_SECONDS: int = 3600


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    jwt_auth: JWTAuth = JWTAuth()


settings = Settings()
