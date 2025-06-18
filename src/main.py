from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

tasks = Dict[int, str]
task_id = 0

class Task(BaseModel):
    description: str
    completed: Optional[bool] = False

@app.post("/task", response_model=Task)
def create_task(task: Task):
    """
    Create a new task
    """
    global task_id
    task_id += 1
    tasks[task_id] = task
    return task

@app.get("/task/{id}", response_model=Task)
def read_task(id: int):
    """
    Get a specific task by id
    """
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[id]

@app.put("/task/{id}", response_model=Task)
def update_task(id: int, task: Task):
    """
    Update an existing task by id
    """
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[id] = task
    return task

@app.delete("/task/{id}")
def delete_task(id: int):
    """
    Delete a specific task by id
    """
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[id]
    return {"message": "Task has been deleted successfully!"}