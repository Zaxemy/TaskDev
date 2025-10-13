from sqlalchemy.ext.asyncio import AsyncSession
from core.models.tasks import Task
from core.schemas.tasks import (
    TaskCreate,
    TaskUpdate,
)
from sqlalchemy import select


async def create_task(session: AsyncSession, task_schema: TaskCreate, user_id: int):
    task_data = task_schema.model_dump()
    task_data['user_id'] = user_id
    task = Task(**task_data)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def get_tasks(session: AsyncSession, user_id: int):
    stmt = select(Task).where(Task.user_id == user_id).order_by(Task.id)
    result = session.execute(stmt)
    return result.scalars().all()   

async def get_task(session: AsyncSession, task_id: int, user_id: int):
    stmt = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def update_task(session: AsyncSession, task_schema: TaskUpdate, task: Task):
    for name, value in task_schema.model_dump(exclude_unset=True).items():
        setattr(task, name, value)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

async def delete_task(session: AsyncSession, task: Task) -> None:
    await session.delete(task)
    await session.commit()
    

