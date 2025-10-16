import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.tasks import TaskCreate, TaskUpdate
from crud import tasks as crud


@pytest.mark.asyncio
async def test_create_and_get_tasks(async_session: AsyncSession):
    created = await crud.create_task(async_session, TaskCreate(title="A", description="d", is_complete=False), user_id=1)
    assert created.id is not None
    assert created.user_id == 1

    tasks = await crud.get_tasks(async_session, user_id=1)
    assert len(tasks) == 1
    assert tasks[0].title == "A"


@pytest.mark.asyncio
async def test_get_task_and_update(async_session: AsyncSession):
    created = await crud.create_task(async_session, TaskCreate(title="B", description=None, is_complete=False), user_id=1)

    fetched = await crud.get_task(async_session, task_id=created.id, user_id=1)
    assert fetched is not None
    assert fetched.title == "B"

    updated = await crud.update_task(async_session, TaskUpdate(title="B2"), fetched)
    assert updated.title == "B2"


@pytest.mark.asyncio
async def test_delete_task(async_session: AsyncSession):
    created = await crud.create_task(async_session, TaskCreate(title="C", description=None, is_complete=False), user_id=1)

    await crud.delete_task(async_session, created)

    missing = await crud.get_task(async_session, task_id=created.id, user_id=1)
    assert missing is None


