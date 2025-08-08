from sqlalchemy.ext.asyncio import AsyncSession
from core.models.tasks import Task
from core.schemas.tasks import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
)
from sqlalchemy import select


async def create_task(session: AsyncSession, task_schema: TaskCreate):
    task = Task(**task_schema.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def get_tasks(session: AsyncSession):
    stmt = select(Task).order_by(Task.id)
    result = await session.execute(stmt)
    tasks = result.scalars().all()
    return tasks

async def get_task(session: AsyncSession, task_id: int):
    return  await session.get(Task, task_id)

async def update_task(session: AsyncSession, task_schema: TaskUpdate, task: Task):
    for name, value in task_schema.model_dump(exclude_unset=True).items():
        setattr(task, name, value)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task
    

