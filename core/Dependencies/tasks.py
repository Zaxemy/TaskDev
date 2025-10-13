from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Path, HTTPException
from crud import tasks as crud
from core.models.db_helper import db_helper
from core.Dependencies.auth import current_user
from core.models.users import User


async def get_task_by_id(
    task_id: Annotated[int, Path], 
    session: AsyncSession = Depends(db_helper.get_db),
    user: User = Depends(current_user)
):
    task = await crud.get_task(session=session, task_id=task_id, user_id=user.id)
    if task is not None:
        return task
    
    raise HTTPException(detail=f'Task {task_id} not found', status_code=404)
