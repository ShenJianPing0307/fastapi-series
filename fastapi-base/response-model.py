from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    address: str = None
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    address: str = None
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut, response_model_include=["address"])
async def create_user(user: UserIn):
    return user


"""
          response_model_exclude_unset=True,
          response_model_exclude_unset=True,
          response_model_exclude=["address"],
          response_model_include=["username","email"]
"""
