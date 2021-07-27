from typing import Optional
from fastapi import FastAPI, Depends, HTTPException


def query_extractor(q: Optional[str] = None):
    if not q:
        raise HTTPException(status_code=400, detail="q is not null")


app = FastAPI(dependencies=[Depends(query_extractor)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
