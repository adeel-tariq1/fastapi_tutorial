from fastapi import FastAPI,HTTPException
import time
from collections import OrderedDict

app= FastAPI()

cache = OrderedDict()

MAX_CACHE_SIZE = 3
CACHE_TTL = 30

users = {
    1: {
        "user_id": 1,
        "name": "Adeel"
    }
}

def get_from_cache(user_id):
    current_time = time.time()
    if user_id not in cache:
         return None
    cached_data, cached_time = cache[user_id]

    if current_time - cached_time < CACHE_TTL: 
                cache.move_to_end(user_id)    #Least Recent Used
                return cached_data
    del cache[user_id]
    return None

def get_from_database(user_id):
    if user_id not in users:
        raise HTTPException(
                  status_code=404,
                  detail="User ID not found"
            )
    result = users[user_id]
    return result

def save_to_cache(user_id, result, current_time):
    cache[user_id] = (result, current_time)
    if len(cache) > MAX_CACHE_SIZE:    #LRU / maximum cache size
            cache.popitem(last=False)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    cached_user = get_from_cache(user_id)

    if cached_user is not None:
        return cached_user
    user = get_from_database(user_id)
    time.sleep(3)
    current_time=time.time()
    save_to_cache(user_id,user,current_time)

    return user

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


    


          
      

        
            