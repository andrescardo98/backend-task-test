from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api import deps
from app.models.task import Task
from app.schemas import task as task_schemas

router = APIRouter()

@router.get("/", response_model=List[task_schemas.Task])
def read_tasks(
    db: deps.SessionDep,
    current_user: deps.CurrentUser,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

@router.post("/", response_model=task_schemas.Task)
def create_task(
    *,
    db: deps.SessionDep,
    task_in: task_schemas.TaskCreate,
    current_user: deps.CurrentUser,
) -> Any:
    task = Task(**task_in.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/{id}", response_model=task_schemas.Task)
def read_task(
    *,
    db: deps.SessionDep,
    id: int,
    current_user: deps.CurrentUser,
) -> Any:
    task = db.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@router.put("/{id}", response_model=task_schemas.Task)
def update_task(
    *,
    db: deps.SessionDep,
    id: int,
    task_in: task_schemas.TaskUpdate,
    current_user: deps.CurrentUser,
) -> Any:
    task = db.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    update_data = task_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{id}", response_model=task_schemas.Task)
def delete_task(
    *,
    db: deps.SessionDep,
    id: int,
    current_user: deps.CurrentUser,
) -> Any:
    task = db.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(task)
    db.commit()
    return task
