from myapi import MiniAPI

app = MiniAPI()

# Sample Database
users = []

@app.get("/")
def home():
    return {
        "message": "Welcome to My Own Framework"
    }

@app.get("/about")
def about():
    return {
        "framework": "MiniAPI",
        "version": "0.1"
    }

@app.get("/users")
def get_users():
    return {
        "users": users
    }

@app.post("/create-user")
def create_user(data):
    users.append(data)
    return {
        "message": "User Created",
        "received": data
    }


@app.put("/update-user")
def update_user(data):
    if users:
        users[0] = data
        return {
            "message": "User Updated",
            "users": users
        }
    return {
        "error": "No user found"
    }


@app.delete("/delete-user")
def delete_user():
    if users:
        deleted_user = users.pop(0)
        return {
            "message": "User Deleted",
            "deleted_user": deleted_user
        }
    return {
        "error": "No user found"
    }

app.run()