from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///TaskDev.sqlite3"
    echo: bool = True

settings = DataBaseSettings()

