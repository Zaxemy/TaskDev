from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(max_length=64,)
    description: str | None = Field(max_length=256,)
    is_complete: bool = False


class TaskResponse(TaskCreate):
    id: int


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        max_length=64,
    )
    description: str | None = Field(
        default=None,
        max_length=256,
    )
    is_complete: bool | None = Field(
        default=None,
    )
