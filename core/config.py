from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path


class DataBaseSettings(BaseModel):
    db_url: str = "sqlite+aiosqlite:///TaskDev.sqlite3"
    echo: bool = True


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600


class JWTAuth(BaseModel):
    private_key_path: Path = Path("certificates") / "private.pem"
    public_key_path: Path = Path("certificates") / "public.pem"
    algorithm: str = "RS256"


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    access_token: AccessToken = AccessToken()
    jwt_auth: JWTAuth = JWTAuth()


settings = Settings()
