from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int
    password : str
    city : str

class UserResponse(BaseModel):
    name : str
    age : int
    city : str
    

@app.get("/users", response_model=UserResponse)
def get_user():
    return {
        "message" : "User Created",
        "name" : "Adeel",
        "age" : 28,
        "password" : 12334,
        "city" : "Rawalpindi"
    }