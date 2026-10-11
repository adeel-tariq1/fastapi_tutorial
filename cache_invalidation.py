from fastapi import FastAPI,HTTPException
import time
from collections import OrderedDict

#TTL / expiration concept
app = FastAPI()

cache = OrderedDict()

MAX_CACHE_SIZE = 3
CACHE_TTL = 30

users = {
    1: {
        "user_id": 1,
        "name": "Adeel"
    }
}



@app.get("/users/{user_id}")
def get_user(user_id: int):

    current_time = time.time()

    # Check cache
    if user_id in cache:

        cached_data, cached_time = cache[user_id]

        # Check whether cache is still valid
        if current_time - cached_time < CACHE_TTL:
            cache.move_to_end(user_id)    #Least Recent Used
            return cached_data
        

        # Cache expired
        del cache[user_id]
    #Error Handling
    if user_id not in users:
            raise HTTPException(
                status_code=404,
                detail="User ID not Found"
            )
    # Expensive operation
    time.sleep(3)

    result = users[user_id]

    # Store result + time
    cache[user_id] = (result, current_time)
    if len(cache) > MAX_CACHE_SIZE:    #LRU / maximum cache size
         cache.popitem(last=False)
    
    


    return result

@app.put("/users/{user_id}")
def put_user(user_id:int,name:str):
    if user_id in users:
        users[user_id].update({
            "user_id":user_id,
            "name":name
        })

    if user_id not in users:
        users[user_id] = {
            "user_id": user_id,
            "name": name
            }

        
    if user_id in cache:
        del cache[user_id]
   
    result = {
            "user_id": user_id,
            "name": name
        }

    return result
