from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

users: List[User] = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "I am revising Fast API development because of YB Dada."}

@app.get("/get-users")
def get_users():
    return users

# Post 
@app.post("/create-user")
def create_user(user: User):
    users.append(user)
    return {"message": f"User created: {user.name}, Age: {user.age}, User:[{user}]"}


# Path Parameter
# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}
