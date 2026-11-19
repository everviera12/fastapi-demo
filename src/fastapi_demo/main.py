from fastapi import FastAPI, Depends, status
from typing import Annotated

# Models
from fastapi_demo.models.models import Tags

from fastapi_demo.routes import users as users_router
from fastapi_demo.routes import animals as animals_router

app = FastAPI()

@app.get("/", tags=[Tags.home], summary="Simple Hello World message")
async def hello_world():
    return {"message": "Hello World!"}

app.include_router(users_router.router)
app.include_router(animals_router.router)