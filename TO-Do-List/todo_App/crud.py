from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from . import models, schema
from typing import List, Optional

def create_task(db: Session, task: schema.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(
    db: Session,
    status: Optional[bool] = None,
    priority: Optional[str] = None,
    sort_by: Optional[str] = "id",
    order: str = "asc",
    skip: int = 0,
    limit: int = 10
) -> List[models.Task]:

    query = db.query(models.Task)

    if status is not None:
        query = query.filter(models.Task.status == status)
    if priority:
        query = query.filter(models.Task.priority == priority)

    if sort_by in ["id", "due_date", "priority"]:
        sort_column = getattr(models.Task, sort_by)
        query = query.order_by(asc(sort_column) if order == "asc" else desc(sort_column))

    return query.offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int, task_data: schema.TaskUpdate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    for key, value in task_data.dict().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return True
