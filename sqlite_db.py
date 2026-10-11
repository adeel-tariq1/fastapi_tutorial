import sqlite3
from fastapi import FastAPI

app=FastAPI()

conn = sqlite3.connect("test.db",check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
Create Table If not Exists Todos(
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed TEXT
)
""")

conn.commit()

@app.get("/")
def home():
    return {
        "message" : "Database Connected"
    }