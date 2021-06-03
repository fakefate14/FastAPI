# introduce to FastAPI
# https://fastapi.tiangolo.com/
# http://127.0.0.1:port/docs

# pip install fastapi
# pip install uvicorn

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# inherit class from BaseModel (pydantic)
class User(BaseModel):
    username:str
    password:str
    level:Optional[str] = "normal"


# decorator
@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://127.0.0.1:5000/hi?name=TestName&reply=TestReply
# http://127.0.0.1:5000/hi?name=TestName
@app.get("/hi")
def hi(name:str,reply:Optional[str]= None):
    return {"Hi":name , "reply":reply}

# http://127.0.0.1:5000/items/1
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/login")
def login(user:User):
    return {"echo": user}



# run
# uvicorn <fileName>:<appInstane> --reload --port 4000