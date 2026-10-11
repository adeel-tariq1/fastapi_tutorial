from fastapi import FastAPI
import time

#TTL / expiration concept
app = FastAPI()

cache = {}

CACHE_TTL = 30


@app.get("/users/{user_id}")
def get_user(user_id: int):

    current_time = time.time()

    # Check cache
    if user_id in cache:

        cached_data, cached_time = cache[user_id]
        # OR
        # cached_data = cache[user_id]["data"]
        # cached_time = cache[user_id]["time"]

        # Check whether cache is still valid
        if current_time - cached_time < CACHE_TTL:
            return cached_data

        # Cache expired
        del cache[user_id]

    # Expensive operation
    time.sleep(3)

    result = {
        "user_id": user_id,
        "name": "Adeel"
    }

    # Store result + time
    cache[user_id] = (result, current_time)

    return result