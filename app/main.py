from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes import auth, tasks


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager Application",
    description="Task management API with user authentication",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def health_check():
    return {"message": "Task Manager API is running"}