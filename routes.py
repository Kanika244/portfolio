from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates  = Jinja2Templates(directory="static/templates")

@router.get("/")
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@router.get("/about")
def about(request:Request):
    return templates.TemplateResponse("about.html",{"request":request})

@router.get("/projects")
def projects(request:Request):
    return templates.TemplateResponse("projects.html",{"request":request})

@router.get("/contact")
def contact(request:Request):
    return templates.TemplateResponse("contact.html",{"request":request})

@router.get("/experiance")
def experiance(request:Request):
    return templates.TemplateResponse("experiance.html",{"request":request})

@router.get("/education")
def education(request:Request):
    return templates.TemplateResponse("education.html",{"request":request})