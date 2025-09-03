from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Todo_Type(BaseModel):
    task_label: str
    status: Optional[bool] = None

app= FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello World"}

todo_list=[]

#get all todos
@app.get("/todos")
async def get_todos():
    updated_list = []
    for index, task in enumerate(todo_list):
        updated_list.append({"id":index + 1, **task.dict() })
    return{"todos": updated_list}

#get single todo
@app.get("/singletodo/{id}")
async def get_todo(id:int):
    return todo_list[id - 1]

#create
@app.post("/todos")
async def create_todos(task: Todo_Type):
    todo_list.append(task)
    return{"message": "Task has been added"}

#update
@app.put("/todos/{id}")
async def update_todo(id:int, updated_task: Todo_Type):

    if 1 <= id <= len(todo_list):
            current_task = todo_list[id - 1]
            current_task.task_label = updated_task.task_label
            current_task.status = updated_task.status
            
            
            return {
                 "message":"Task has been updated."
                   ,"task": current_task.dict()
                   }       
    return{"message": "Update was not possible because ID was not valid."}

#delete

@app.delete("/todos/{id}")

async def delete_todo(id:int):
    if 1 <= id <= len(todo_list):
            todo_list.pop(id-1)
            return {"message":"Task has been deleted."}      
    return{"message": "no task found with this id"}