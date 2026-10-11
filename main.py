from fastapi import FastAPI

app = FastAPI()

#get request
@app.get("/")
def home():
    return{"mesaage": "Hello World From Adeel Tariq"}

@app.get("/about")
def about():
    return{"message":"We are here to provide you the best AI services"}

@app.get("/users/{user_id}")
def get_user(user_id : int):
    return {"User ID" : user_id}

#default param
@app.get("/names")
def get_name(name : str = None):
    return {"name" : name}

#multiple query param
@app.get("/items")
def items(name : str = None , price : int = 100):
    return {
        "name" : name,
        "price" : price
    }