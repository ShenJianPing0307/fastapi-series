from typing import Optional, Union, List
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


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    address: str = None
    fullname: Optional[str] = None


def fake_password_hasher(raw_password: str):
    return "secret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    # user_in_obj = UserIn(username="zhang san",
    #                      password="123456",
    #                      email="user@example.com",
    #                      address="zhang san street",
    #                      full_name="zhangsan")
    # print('hello')
    # print(user_in_obj.dict(),type(user_in_obj))
    # print(user_in, type(user_in))
    # print(user_in.dict(), type(user_in.dict()))
    user_saved = fake_save_user(user_in)
    return user_saved


@app.post("/response/model", response_model=List[UserOut])
async def response_model():
    user_list = [
        {
            'username': 'zhangsan',
            'password': '123456',
            'email': 'user@example.com',
            'address': 'zhangsanstreet',
            'full_name': 'zhangsan'
        },
        {
            'username': 'lisi',
            'password': '123456',
            'email': 'user@example.com',
            'address': 'lisistreet',
            'full_name': 'lisi'
        }
    ]
    return user_list


from typing import Dict
from fastapi import FastAPI

app = FastAPI()


@app.get("/apple/dict/", response_model=Dict[str, float])
async def apple_dict():
    return {"apple": 3.14, "pear": 5.12}
