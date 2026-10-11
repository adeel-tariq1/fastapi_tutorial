from fastapi import FastAPI , Depends, Header ,HTTPException
from pydantic import BaseModel

app = FastAPI()
#auth example
def verify_token(token : str = Header(None)):
    if token != "mysecretapi":
        raise HTTPException(
            status_code=401,
            detail= "Unauthorized"
        )
    return {
        "Message" : "Access Granted",
        "User" : "Authorized User"
    }

@app.get("/token")
def token(user = Depends(verify_token)):
    return {
        "user" : user
    }

#Depends using same function in different APIs
# def user():
#     return {
#         "Name" : "Adeel"
#     }
# @app.get("/home")
# def home(data=Depends(user)):
#     return data

# @app.get("/dashboard")
# def dashboard(users = Depends(user)):
#     return users