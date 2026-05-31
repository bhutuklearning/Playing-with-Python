from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    name: str
    age: int


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "I am revising Fast API development because of YB Dada."}

# Path Parameter
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Post 
@app.post("/create-user")
def create_user(user: User):
    return {"message": f"User created: {user.name}, Age: {user.age}"}

