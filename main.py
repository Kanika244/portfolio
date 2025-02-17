from fastapi import FastAPI
from routes import router 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")
templates  = Jinja2Templates(directory="static/templates")

app.include_router(router)
