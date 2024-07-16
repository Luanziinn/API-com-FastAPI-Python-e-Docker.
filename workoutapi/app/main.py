from fastapi import FastAPI
from .database import engine
from .routers import atleta
from . import models
from fastapi_pagination import add_pagination

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(atleta.router)

add_pagination(app)
