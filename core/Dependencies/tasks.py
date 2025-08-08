from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Path, HTTPException
from crud import tasks as crud
from core.models.db_helper import db_helper


async def get_task_by_id(task_id: Annotated[int, Path], session: AsyncSession = Depends(db_helper.get_db)):
    task = await crud.get_task(session=session,task_id=task_id)
    if task is not None:
        return task
    
    raise HTTPException(detail=f'Task {task_id} not found', status_code=404)
