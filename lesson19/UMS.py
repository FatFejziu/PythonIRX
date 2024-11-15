from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class User(BaseModel):
    id: int
    name:str
    age:int
    email:str

@app.post("/users/")
async def create_user(perdoruesi:User):
    return perdoruesi