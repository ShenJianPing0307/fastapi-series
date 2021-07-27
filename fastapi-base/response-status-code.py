from fastapi import FastAPI, status

app = FastAPI()


@app.post("/status_attribute/", status_code=status.HTTP_200_OK)
async def status_code():
    return {"status_code": status.HTTP_200_OK}


@app.post("/status_code/", status_code=201)
async def status_code():
    return {"status_code": 200}
