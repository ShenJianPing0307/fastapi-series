from fastapi import FastAPI

app = FastAPI()


@app.post("/docs/item",
          tags=["items"],
          summary="create an item",
          )
async def create_item():
    """
    create an item with all infomation:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **...**
    """
    return {"info": "create item"}

@app.post("/create/item",
          tags=["items"],
          summary="create an item",
          description="this is a item,about ...",
          response_description="the created item ...",
          deprecated=True
          )
async def create_item():
    return {"info": "create item"}


@app.get("/get/item", tags=["items"])
async def read_items():
    return {"info": "get items"}


@app.get("/users", tags=["users"])
async def read_users():
    return {"info": "get users"}
