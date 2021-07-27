import time
from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/items/")
async def get_items():
    items = [
        {"name": "apple", "price": "1.12"},
        {"name": "pear", "price": "3.14"}
    ]
    return items
