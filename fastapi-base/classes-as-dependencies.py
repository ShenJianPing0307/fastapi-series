from typing import Optional
from fastapi import Depends, FastAPI

app = FastAPI()

items = [
    {"name": "apple", "price": "1.12"},
    {"name": "pear", "price": "3.14"}
]


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    result = items[commons.skip:commons.skip + commons.limit]
    response.update({"result": result})
    return response
