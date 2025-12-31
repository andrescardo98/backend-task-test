from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.models.task import TaskStatus

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
