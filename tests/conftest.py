import asyncio
import pytest
from typing import AsyncGenerator

from fastapi import Depends
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from core.models.base import Base
from core.models.users import User as users_models  
from core.models.tasks import Task as tasks_models  
from core.models.db_helper import DatabaseHelper, db_helper
from core.config import settings
from core.Dependencies import auth as auth_deps
from core.models.users import User


TEST_DB_URL = settings.db.test_db_url


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_engine():
    engine = create_async_engine(TEST_DB_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield engine
    finally:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        await engine.dispose()


@pytest.fixture()
async def async_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    Session = async_sessionmaker(bind=test_engine, autoflush=False, autocommit=False, expire_on_commit=False)
    async with Session() as session:
        yield session


@pytest.fixture(autouse=True)
def override_db(async_session: AsyncSession):
    async def _get_db() -> AsyncGenerator[AsyncSession, None]:
        async with async_session.bind.connect() as _:
            yield async_session

    app.dependency_overrides[db_helper.get_db] = _get_db
    yield
    app.dependency_overrides.pop(db_helper.get_db, None)


@pytest.fixture()
def test_user() -> User:
    
    class _U:
        pass
    user = _U()
    user.id = 1
    user.email = "test@example.com"
    user.hashed_password = "hashed"
    user.is_active = True
    user.is_superuser = False
    user.is_verified = True
    user.username = "tester"
    return user


@pytest.fixture(autouse=True)
def override_current_user(test_user: User):
    async def _current_user_override():
        return test_user

    app.dependency_overrides[auth_deps.current_user] = _current_user_override
    yield
    app.dependency_overrides.pop(auth_deps.current_user, None)


@pytest.fixture()
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as c:
            yield c


