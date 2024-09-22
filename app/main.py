from fastapi import FastAPI, Depends, HTTPException, Request
from app import crud, models, schemas, auth
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .utils import get_ip, get_ip_location, get_weather
from .models import RequestLog
from datetime import datetime
import json

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#middleware para obtener la ip del cliente
@app.middleware("http")
async def log_ip_and_weather(request: Request, call_next):
    #ip del cliente
    client_ip = get_ip()

    #Si ip no válida
    if not client_ip:
        raise HTTPException(status_code=400, detail="Could not determine IP address")

    #país de la ip
    country_json = get_ip_location(client_ip)
    country = country_json.get("country")

    #si no se obtiene el país
    if not country:
        raise HTTPException(status_code=400, detail="Could not determine country from IP")

    #clima del país
    weather_info_json = get_weather(country)
    weather_info = json.dumps(weather_info_json)

    # Guardar datos en db
    with SessionLocal() as db:
        log = RequestLog(ip_address=client_ip, country=country, weather=weather_info, timestamp=datetime.utcnow())
        db.add(log)
        db.commit()

    #continuacion de solicitud
    response = await call_next(request)
    return response

@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), request: Request = None):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.Task])
def get_tasks(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), request: Request = None):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), request: Request = None):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), request: Request = None):
    return crud.update_task(db, task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), request: Request = None):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.get("/logs", response_model=list[schemas.RequestLog])
def get_logs(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    logs = crud.get_request_logs(db)
    return logs


