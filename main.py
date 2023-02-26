from fastapi import FastAPI, Request,Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Response, BackgroundTasks
from fastapi.responses import FileResponse
import io
import os
import uvicorn

from pathlib import Path
import logging


from fastapi.middleware.cors import CORSMiddleware







app = FastAPI()
app.mount("/static", StaticFiles(directory= os.path.dirname(os.path.abspath(__file__))+"/static"), name="static")
app.mount("/javascript", StaticFiles(directory= os.path.dirname(os.path.abspath(__file__))+"/javascript"), name="javascript")


origins = [
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=os.path.dirname(os.path.abspath(__file__)))



@app.get("/") 
async def root():
    return {"message": "Hello World"}


@app.get("/resume")
async def get_resume():
    some_file_path = "static/DineshP_Feb_CV.pdf"
    return FileResponse(some_file_path)


@app.get("/index", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("index.html",context={"request":request});


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)



