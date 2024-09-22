from sqlalchemy.orm import Session
from . import models, schemas
from .models import RequestLog

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(task_name=task.task_name, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.task_name = task.task_name
        db_task.description = task.description
        db_task.status = task.status
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False


def get_request_logs(db: Session):
    return db.query(RequestLog).all()
