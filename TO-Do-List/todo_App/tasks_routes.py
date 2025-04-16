from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, schema, models
from .database import SessionLocal, engine
from .auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/tasks", tags=["Tasks"], dependencies=[Depends(JWTBearer())])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.TaskOut)
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/", response_model=List[schema.TaskOut])
def read_tasks(
    db: Session = Depends(get_db),
    status: Optional[bool] = None,
    priority: Optional[str] = None,
    sort_by: Optional[str] = Query("id", enum=["id", "due_date", "priority"]),
    order: Optional[str] = Query("asc", enum=["asc", "desc"]),
    skip: int = 0,
    limit: int = 10
):
    return crud.get_tasks(db, status, priority, sort_by, order, skip, limit)

@router.get("/{task_id}", response_model=schema.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=schema.TaskOut)
def update_task(task_id: int, task: schema.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return
