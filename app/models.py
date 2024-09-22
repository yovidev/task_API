from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    description = Column(String)
    status = Column(Enum("pending", "completed", name="task_status"), default="pending")


class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, index=True)
    country = Column(String, index=True)
    weather = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)