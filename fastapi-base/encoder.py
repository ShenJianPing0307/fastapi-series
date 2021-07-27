from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    address: str = None
    full_name: Optional[str] = None


@app.post("/user/")
async def create_user(user: UserIn):
    json_compatible_data = jsonable_encoder(user)
    print(type(json_compatible_data))  # <class 'dict'>
    return user
