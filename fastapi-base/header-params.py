from typing import Optional, List
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None, convert_underscores=True), x_token: Optional[List[str]] = Header(None)):
    return {"User-Agent": user_agent, "x_token": x_token}
