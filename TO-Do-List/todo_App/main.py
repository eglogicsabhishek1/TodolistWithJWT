from fastapi import FastAPI
from . import models
from .database import engine
from .tasks_routes import router as TaskRouter
from .auth.auth_routes import router as AuthRouter

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API with FastAPI & MySQL")

# Include routes
app.include_router(AuthRouter)
app.include_router(TaskRouter)
