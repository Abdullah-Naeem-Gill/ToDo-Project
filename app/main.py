from fastapi import FastAPI
from database import SessionLocal, engine
import models
from api import users, tasks
from database import get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
