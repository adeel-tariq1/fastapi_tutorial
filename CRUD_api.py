from fastapi import FastAPI
from pydantic import BaseModel , Field

app = FastAPI()

class Address(BaseModel):
    city : str
    code : int



class Todos(BaseModel):
    name : str
    age : int
    status : bool
    address : Address

todos = []

@app.post("/todos")
def create_todo(todo :Todos):
    todos.append(todo)
    return {
        "message" : "User Added",
        "data" : todo
    }

@app.get("/todos")
def get_todos():
    return todos

#to get only one data
@app.get("/todos/{todo_name}")
def get_todo(todo_name: str):

    all_users = []

    for todo in todos:

        if todo.name == todo_name:
            all_users.append(todo)
 
    if all_users:
        return all_users

    return {"error": "todo not found"}

#Update the existing Data
@app.put("/todos")
def updated_todo(todo_name:str, update_todo : Todos):
    for index,todo in enumerate(todos):
        if todo.name.lower() == todo_name.lower():
            todos[index] = update_todo
            return {
                "message" : "Todo Updated",
                "data" : update_todo
            }
    return {"error": "todo not found"}    

#delete Data
@app.delete("/todos")
def delete_todo(todo_name:str):
    for index,todo in enumerate(todos):
        if todo.name.lower() == todo_name.lower():
            deleted_todo = todos.pop(index)
            return {
                            "message" : "Todo Deleted",
                            "data" : deleted_todo
                        }
    return {"error": "todo not found"}    
            