from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    # Assume current user ID is 1 for simplicity; implement user management properly
    return crud.create_task(db=db, task=task, user_id=1)

@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    # Assume current user ID is 1 for simplicity; implement user management properly
    return crud.get_tasks_by_user(db=db, user_id=1)
