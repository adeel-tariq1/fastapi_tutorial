from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

@app.get("/multiple-data")
async def multiple_data():
    async with httpx.AsyncClient() as client:
        post_response, user_response = await asyncio.gather(
            client.get("https://jsonplaceholder.typicode.com/posts/1"),
            client.get("https://jsonplaceholder.typicode.com/users/1")
        )

    return {
        "post": post_response.json(),
        "user": user_response.json()
    }