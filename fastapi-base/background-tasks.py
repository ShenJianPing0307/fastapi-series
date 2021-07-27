from fastapi import BackgroundTasks, FastAPI, Depends
from typing import Optional

app = FastAPI()


def write_log(message: str):
    with open("log.txt", mode="a") as f:
        f.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query:{q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/dependency/background_tasks")
async def write_log(q: str = Depends(get_query)):
    if q:
        return {"message": "write log in the background"}
