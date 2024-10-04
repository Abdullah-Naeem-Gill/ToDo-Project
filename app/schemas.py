from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: str

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_by: User

    class Config:
        orm_mode = True
