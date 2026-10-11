from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse
import os,shutil

app = FastAPI()
#since fastapi is running locally on my pc...so it would create a copy of uploaded item on my pc and later use it if asked.
UPLOAD_DIR = "uploads"
#check if Upload folder exist. If not then create it.
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#STEP-2:Static file set-up
#URL: HTTP://127.0.0.1:8080/FILES/<FILEnAME>
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

@app.post("/upload")
def upload_file(file: UploadFile= File(...)):
    filename = file.filename
    file_path= os.path.join(UPLOAD_DIR,filename)

    if not file.filename:
        raise HTTPException(status_code=401,detail="File not selected")

    with open (file_path ,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)  #copying the file on server/pc

        return {
            "messsage":"File Uploaded successfully",
            "filename":filename,
            "file_url":f"http://127.0.0.1:8000/files/{filename}"
        }


@app.get("/files/{filename}")
def get_file(filename:str):
    file_path= os.path.join(UPLOAD_DIR,filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return {
        "file_url":f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/",response_class=PlainTextResponse)
def home():
    return "Fastapi is connected \n Upload a File"