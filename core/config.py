from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path


class DataBaseSettings(BaseModel):
    db_url: str = "sqlite+aiosqlite:///TaskDev.sqlite3"
    echo: bool = True


class JWTAuth(BaseModel):
    SECRET: str = "993Nqs9GkGgF7NwDmJc3xE2wI6S1De3XPreg70SXu-E"

    ALGORITHM: str = "HS256"
    LIFETIME_SECONDS: int = 3600


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    jwt_auth: JWTAuth = JWTAuth()


settings = Settings()
