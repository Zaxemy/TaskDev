from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

class DataBaseSettings(BaseModel):
    db_url: str = "sqlite+aiosqlite:///TaskDev.sqlite3"
    echo: bool = True

class JWTAuth(BaseModel):
    private_key_path: Path = Path("certificates") / "private.pem"
    public_key_path: Path = Path("certificates") / "public.pem"
    algorithm: str = "RS256"


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()

    jwt_auth: JWTAuth = JWTAuth()



settings = Settings()