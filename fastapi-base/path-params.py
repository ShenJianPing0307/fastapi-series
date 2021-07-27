from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/path/parameters")
def path_params_1():
    return {"message":"This is path_params_1"}

@app.get("/path/{parameters}")
def path_params_2(parameters:str):
    return {"message":parameters}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# 预设值


class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/model/{model_name}")
async def get_model(model_name:ModelName):
    return {"model_name":model_name.alexnet}

# 包含路径
@app.get("/file/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}

class CityName(str,Enum):
    Xian = "Xian china"
    Shanghai = "Shanghai china"

@app.get("/enum/{city}")
async def city_info(city:CityName):
    if city == CityName.Xian:
        return {"info":city}
    if  city == CityName.Shanghai:
        return {"info":city}