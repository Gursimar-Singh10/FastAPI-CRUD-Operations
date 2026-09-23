from fastapi import FastAPI , Depends
from pydantic import BaseModel
from models import TodoModel
from sqlalchemy.orm import Session
from database import engine , Sessionlocal
from typing import Optional , List

# HERE ALL I USE SQLALCHEMY

app = FastAPI() #create an instance of fastAPI

TodoModel.metadata.create_all(bind=engine) # create the table in database

# todos = [] # create an empty list to store todos , in memory db

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id : int

    class Config:
        orm_mode = True



def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()







@app.get("/todos" , response_model=List[TodoResponse])
def get_todos(db : Session= Depends(get_db) ):
    todos=db.query(TodoModel).all()
    return todos

@app.get("/todos/{todo_id}" , response_model=TodoResponse)
def get_todo(todo_id: int , db : Session= Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    return todo  


@app.post("/todos" , response_model=TodoResponse)
def create_todo(todo: TodoBase , db : Session= Depends(get_db)):
    db_todo = TodoModel(title=todo.title , description=todo.description , completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo



@app.delete("/todos/{todo_id}" , response_model=TodoResponse)
def delete_todo(todo_id: int , db : Session= Depends(get_db)):
      todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
      db.delete(todo)
      db.commit()
      return todo

