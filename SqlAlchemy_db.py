from sqlalchemy import create_engine,Column,INTEGER,String,Boolean
from sqlalchemy.orm import declarative_base , sessionmaker,Session
from fastapi import FastAPI,Depends

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
    name =Column(String)
    status = Column(Boolean)

Base.metadata.create_all(bind=engine)

def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db : Session = Depends(get_db)):
    return {
        "message":"Database is connected to your server"
    }