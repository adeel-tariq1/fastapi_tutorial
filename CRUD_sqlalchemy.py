# Create Operation with SqlAlchemy
from sqlalchemy import create_engine,Column,INTEGER,String
from sqlalchemy.orm import declarative_base , sessionmaker,Session
from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()
DATABASE_URL = "sqlite:///./try.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" :False}
)

localsession = sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(INTEGER,primary_key=True,)
    title =Column(String)
    status = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()

#Create Data
@app.post("/todos")
def create_todo(title:str,db : Session = Depends(get_db)):
    todos = Todo(title=title,status="True")
    db.add(todos)
    db.commit()
    db.refresh(todos)
    return {
        "message":"Todo Created Successfully",
        "Data" : todos
    }
#Delete Data by Id
@app.delete("/todos")
def delete_todo(id:int,db : Session =Depends(get_db)):
        todo = db.query(Todo).filter(Todo.id == id).first()
        if not todo:
            raise HTTPException(status_code=404,detail="Id not Found")

        db.delete(todo)
        db.commit()

            
        return {
            "message":"Todo Deleted Successfully",
            "Data" : todo
        }

#Read All Data
@app.get("/todos")
def get_todo(db : Session = Depends(get_db)):
     todo = db.query(Todo).all()

     return {
          "Total Data" :len(todo),
          "Data":todo 
     }
#Read Data By ID
@app.get("/todos/{todo_id}")
def get_todo_byid(todo_id:int,db:Session=Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id== todo_id).first()

     if not todo:
          raise HTTPException (status_code=404,detail="Data not found")
     return{
          "data" : todo
     }

#Update the existing Data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db :Session=Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()

     if not todo:
               raise HTTPException (status_code=404,detail="Data not found")

     todo.title = title
     db.commit()
     db.refresh(todo)

     return{
          "message": "Todo Updated",
          "Data": todo
     }