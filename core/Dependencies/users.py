from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Path, HTTPException
from crud import users as crud
from core.models.db_helper import db_helper


async def get_user_by_id(user_id: Annotated[int, Path], session: AsyncSession = Depends(db_helper.get_db)):
    user = await crud.get_task(session=session,user_id=user_id)
    if user is not None:
        return user
    
    raise HTTPException(detail=f'Task {user_id} not found', status_code=404)