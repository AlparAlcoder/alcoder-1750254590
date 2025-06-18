```markdown
# FastAPI Task Manager

This application is a simple task management API built using FastAPI. It allows for the creation, retrieval, updating, and deletion of tasks.

## Models

### Task
A task is represented by the following model:

```python
class Task(BaseModel):
    description: str
    completed: Optional[bool] = False
```
Fields:
- `description` (str): A brief description of the task.
- `completed` (Optional[bool]): The completion status of the task. Defaults to `False`.

## Endpoints

### POST /task
Creates a new task.

Parameters:
- `task` (Task): A `Task` object to be created.

Returns:
- A `Task` object that was created.

Example:
```python
{
    "description": "Clean the house",
    "completed": false
}
```

### GET /task/{id}
Retrieves a task by id.

Parameters:
- `id` (int): The id of the task to retrieve.

Returns:
- The `Task` object with the corresponding id.

### PUT /task/{id}
Updates an existing task by id.

Parameters:
- `id` (int): The id of the task to update.
- `task` (Task): A `Task` object with the updated fields.

Returns:
- The updated `Task` object.

### DELETE /task/{id}
Deletes a task by id.

Parameters:
- `id` (int): The id of the task to delete.

Returns:
- A message indicating successful deletion.

## Important Notes
If an id that does not exist in the task list is provided in the `GET`, `PUT`, or `DELETE` endpoints, a `404` error with the detail "Task not found" will be returned.

## Dependencies
This application requires the following dependencies:
- `fastapi`
- `pydantic`
```
