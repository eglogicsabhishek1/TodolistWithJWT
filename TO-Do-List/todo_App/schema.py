from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskBase(BaseModel):
    description: str
    status: bool
    priority: str
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str