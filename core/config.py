from pydantic_settings import BaseSettings # Заменить на dataclasses
from pydantic import BaseModel
from pathlib import Path

class DataBaseSettings(BaseModel):
    db_url: str = "sqlite+aiosqlite:///TaskDev.sqlite3"
    echo: bool = True

class JWTAuth(BaseModel):
    private_key_path: Path = Path("certificates") / "private.pem" # Заменить на чтение из env
    public_key_path: Path = Path("certificates") / "public.pem" # Заменить на чтение из env
    algorithm: str = "RS256"


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()

    jwt_auth: JWTAuth = JWTAuth()

# Добавить конфиг сервера

settings = Settings()