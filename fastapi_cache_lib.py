
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
import asyncio
import time

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.inmemory import InMemoryBackend


# 1. Initialize the cache when the application starts
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    FastAPICache.init(InMemoryBackend())
    print("Cache initialized!")

    yield

    print("Application is shutting down!")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():
    return {"message": "FastAPI is running"}


@app.get("/users/{user_id}")
@cache(expire=30)
async def get_user(user_id: int):
    print(f"Fetching user {user_id} from the source...")

    # Simulate a slow operation
    await asyncio.sleep(3)

    return {
        "user_id": user_id,
        "name": "Adeel",
        "fetched_at": time.time()
    }