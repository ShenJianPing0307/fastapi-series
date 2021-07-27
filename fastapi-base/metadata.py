from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Docs Test",
    description="FastAPI Application Params Test",
    version="1.1.1",
    docs_url="/docs"
)


@app.get("items")
async def read_items():
    return {"info": "read_items"}
