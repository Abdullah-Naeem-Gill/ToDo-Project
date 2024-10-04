from sqlalchemy.orm import Session
import models, schemas
import bcrypt

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), created_by=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.created_by == user_id).all()

def assign_task(db: Session, task_id: int, user_id: int):
    # Here you would implement task assignment logic
    pass

def unassign_task(db: Session, task_id: int, user_id: int):
    # Here you would implement task unassignment logic
    pass
