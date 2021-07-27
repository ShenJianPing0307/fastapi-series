from fastapi import FastAPI

app = FastAPI()


async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
#
# @app.get("/items/")
# async def get_items():
#     db = next(get_db())
#     return [{"name": "apple"}, {"name": "pear"}]
