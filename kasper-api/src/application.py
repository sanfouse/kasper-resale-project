from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from src.database.connection import database
from src.routers import users, universities, adverts, dormitories, categories
from fastapi.templating import Jinja2Templates
from fastapi_pagination import add_pagination

app = FastAPI()
templates = Jinja2Templates(directory="templates")

add_pagination(app)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


app.include_router(users.router)
app.include_router(categories.router)
app.include_router(adverts.router)
app.include_router(dormitories.router)
app.include_router(universities.router)