from typing import Optional
from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel, Field
from datetime import date


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="the description ...", max_length=20)
    price: float = Field(..., ge=2, description="price")
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "apple",
                "description": "this is a fruit ...",
                "price": 3.14,
                "tax": 1.2
            }
        }


class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    birthday: date


app = FastAPI()


@app.post("/multi/params/{item_id}")
async def multi_params(
        *,
        item_id: int = Path(..., title="item id ...", ge=1, le=10),
        q: Optional[str] = None,
        item: Optional[Item] = None,
        user: User,
        importance: int = Body(...)
):
    results = {"item_id": item_id, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.post("/single/value")
async def single_value(importance: int = Body(...)):
    return {"importance": importance}


@app.post("/items/")
async def create_item(item: Item = Body(..., embed=True)):
    return {"item": item}
