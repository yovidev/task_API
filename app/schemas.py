from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    task_name: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    status: str

class Task(TaskBase):
    id: int
    status: str

    class Config:
        orm_mode = True


class RequestLog(BaseModel):
    id: int
    ip_address: str
    country: str
    weather: str
    timestamp: datetime

    class Config:
        orm_mode = True