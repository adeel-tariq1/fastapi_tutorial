from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime,timedelta,timezone

app = FastAPI()

SECRET_KEY="mysecretkey"
ALGORITHM="HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#create token will be same as in Jwt authentication
def create_token(data : dict):
    to_encode=data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=20)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    username = form_data.username
    password = form_data.password

    if username != "admin" or password != "1234":
        raise HTTPException (
            status_code=401,
            detail="Invalid Username or password"
        )
    token = create_token({
        "sub": username
    })
    return {
        "access_token":token,
        "token_type" : "bearer"
    }

def verify_token(token:str=Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,
                            detail="Invalid or Expire token")
    

@app.get("/secure")
def secure(user=Depends(verify_token)):
    return{
        "message":"Secured Data Accessed",
        "User":user
    }