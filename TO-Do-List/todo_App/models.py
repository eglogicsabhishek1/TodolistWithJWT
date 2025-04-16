from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    status = Column(Boolean, default=False)
    priority = Column(String(10), default="Medium")
    due_date = Column(Date, nullable=True)
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
