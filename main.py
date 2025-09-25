from fastapi import FastAPI
import uvicorn
from api.tasks import router as tasks_router
from core.Dependencies.auth import fastapi_users
from core.authentication.auth_backend import auth_backend
from core.schemas import users as user_schemas


app = FastAPI()

app.include_router(tasks_router)


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(user_schemas.UserRead, user_schemas.UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(user_schemas.UserRead, user_schemas.UserUpdate),
    prefix="/users",
    tags=["users"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=6969, reload=True)
