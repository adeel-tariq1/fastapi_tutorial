import asyncio
import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/async-wait")
async def async_wait():
    await asyncio.sleep(3)
    return {"message": "Async finished"}

@app.get("/quick")
async def quick():
    return {"message": "Quick response"}