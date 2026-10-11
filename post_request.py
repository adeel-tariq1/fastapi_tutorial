from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

class Address(BaseModel):
    city: str
    pincode : int

class User(BaseModel):
    name : str = Field(..., description= "Must not be a single character")
    age : int = Field(..., description="Must be an integer")
    address : Address

#Json data input
@app.post("/Create_user")
def data(user:User):
    return {
        "message": "User Created",
        "data" : user
    }