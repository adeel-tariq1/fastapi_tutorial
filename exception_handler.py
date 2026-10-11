from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class Usernotfound(Exception):
    def __init__(self, name):
        self.name = name

@app.exception_handler(Usernotfound)
def user_not_found(request : Request , exc : Usernotfound):
    return JSONResponse(
        status_code=404,
        content={
            "status" : "Error",
            "message": f"User {exc.name} not found"

        }
    )

@app.get("/users/{name}")
def get_users(name : str):
    if name != "Adeel":
        raise Usernotfound(name)
    return {
        "message" : "User Detail",
        "Name" : "Adeel"
    }