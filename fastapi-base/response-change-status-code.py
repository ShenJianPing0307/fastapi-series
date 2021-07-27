from fastapi import FastAPI, Response, status

app = FastAPI()

tasks = {"k1": "v1"}


@app.put("/get_or_create_task/{task_id}", status_code=200)
def get_or_create_task(task_id: str, response: Response):
    if task_id not in tasks:
        tasks[task_id] = "this task not in tasks before"
        response.status_code = status.HTTP_201_CREATED
    return tasks
