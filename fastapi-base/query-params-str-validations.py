from fastapi import FastAPI
from fastapi import Query
from typing import List

app = FastAPI()

@app.get("/query/validations")
def query_params_validate(
        value: str = Query(...,min_length=3,max_length=6,regex="^z"),
        values: List[str] = Query(["V1","V2"])
):

    return value,values