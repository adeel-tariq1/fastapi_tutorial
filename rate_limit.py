from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

from slowapi import Limiter                    #Creates the rate-limiting mechanism
from slowapi.errors import RateLimitExceeded   #Exception raised when a configured limit is exceeded 
from slowapi.util import get_remote_address    #Gets the client's IP address to identify the client
from slowapi.middleware import SlowAPIMiddleware  #Integrates SlowAPI with the request/response pipeline

app = FastAPI()

#Limiter setup
limiter = Limiter(key_func=get_remote_address)  #key_func tells it how to identify each client
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

#Error Handling
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request:Request,exc:RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail":"Too many requests"
        }
    )

#Rate limiter API
@app.get("/data")
@limiter.limit("5/minute")
def get_data(request:Request):
    return{
        "message":"Successfully connected"
    }