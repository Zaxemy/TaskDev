from fastapi import APIRouter
from core.models.tasks import Task
from core.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.models.db_helper import db_helper
from crud import tasks as crud
from core.Dependencies.tasks import get_task_by_id
from core.Dependencies.auth import current_user
from core.models.users import User


router = APIRouter(prefix="/tasks")


@router.get(
    "/", response_model=list[TaskResponse], tags=["Tasks"], summary="Get All Tasks"
)
async def get_tasks(
    session: AsyncSession = Depends(db_helper.get_db),
    user: User = Depends(current_user)
):
    return await crud.get_tasks(session=session, user_id=user.id)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=201,
    tags=["Tasks"],
    summary="Create Task",
)
async def create_task(
    task_schema: TaskCreate, 
    session: AsyncSession = Depends(db_helper.get_db),
    user: User = Depends(current_user)
):
    return await crud.create_task(task_schema=task_schema, session=session, user_id=user.id)


@router.get(
    "/{task_id}/", response_model=TaskResponse, tags=["Tasks"], summary="Get task by id"
)
async def get_task(task: Task = Depends(get_task_by_id)):
    return task


@router.patch(
    "/{task_id}/", response_model=TaskResponse, tags=["Tasks"], summary="Edit task"
)
async def update_task(
    task_schema: TaskUpdate,
    task: Task = Depends(get_task_by_id),
    session: AsyncSession = Depends(db_helper.get_db),
):
    return await crud.update_task(session=session, task_schema=task_schema, task=task)


@router.delete("/{task_id}/", status_code=204, tags=["Tasks"], summary="delete task")
async def delete_task(
    task: Task = Depends(get_task_by_id),
    session: AsyncSession = Depends(db_helper.get_db),
):
    await crud.delete_task(task=task, session=session)
