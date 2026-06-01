from myapi import MiniAPI

app = MiniAPI()

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


@app.post("/user")
def create_user(data):

    return {
        "message": "User Created",
        "received": data
    }


app.run()