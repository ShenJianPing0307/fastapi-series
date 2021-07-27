from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/multi/params/{item_id}")
async def multi_params(item_id: int, skip: int = 1, limit: Optional[int] = None):
    item = {"item_id":item_id,"skip":skip}
    if limit:
        item.update({"limit":limit})
    return item



@app.get("/query/bool/conversion")
async def type_conversion(param: bool = False):
    return param


@app.get("/query")
async def page_limit(skip: int = 1, limit: Optional[int] = None):
    if limit:
        return {"skip": skip, "limit": limit}
    return {"skip": skip}
