from fastapi import APIRouter, HTTPException
from core.models.tasks import Task
from core.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.models.db_helper import db_helper
from crud import tasks as crud
from core.schemas.tasks import TaskCreate
from core.Dependencies.tasks import get_task_by_id


router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
async def get_tasks(session: AsyncSession = Depends(db_helper.get_db)):
    return await crud.get_tasks(session=session)


@router.post("/", response_model=TaskResponse,status_code=201)
async def create_task(task_schema: TaskCreate, session: AsyncSession = Depends(db_helper.get_db)):
    return await crud.create_task(task_schema=task_schema, session=session)

@router.get("/{task_id}/", response_model=TaskResponse)
async def get_task(task: Task = Depends(get_task_by_id)):
    return task

@router.patch("/{task_id}/", response_model=TaskResponse)
async def update_task(
    task_schema: TaskUpdate,
    task: Task = Depends(get_task_by_id),
    session: AsyncSession = Depends(db_helper.get_db),
):
    
    
    return await crud.update_task(
        session=session,
        task_schema=task_schema,
        task=task  
    )
@router.delete("/{task_id}/",status_code=204)
async def delete_task(task: Task = Depends(get_task_by_id),session: AsyncSession = Depends(db_helper.get_db)):
    await crud.delete_task(task=task, session=session)

    