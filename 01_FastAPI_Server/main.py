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

# Get all users
@app.get("/get-users")
def get_users():
    return users

# Get user by ID
@app.get("/get-user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"message": "User not found"}

# Post 
@app.post("/create-user")
def create_user(user: User):
    users.append(user)
    return {"message": f"User created: {user.name}, Age: {user.age}, User:[{user}]"}

# Update User
@app.put("/update-user/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": f"User updated: {updated_user.name}, Age: {updated_user.age}, User:[{updated_user}]"}
    return {"message": "User not found"}

# Delete User
@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return {"message": f"User deleted: {deleted_user.name}, Age: {deleted_user.age}, User:[{deleted_user}]"}
    return {"message": "User not found"}


# Path Parameter
# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}
