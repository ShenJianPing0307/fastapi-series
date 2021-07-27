from fastapi import FastAPI
from fastapi import Path

app = FastAPI()

@app.get("/path/{num}")
def path_params_validate(
        num:int = Path(...,title="input your num",description="description num",ge=1,le=5 )
):
    return num