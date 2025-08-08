from fastapi import FastAPI
import uvicorn
from api.tasks import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=6969, reload=True)