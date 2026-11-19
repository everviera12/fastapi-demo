from fastapi import FastAPI, Depends, status
from typing import Annotated

# Database simulation
from fastapi_demo.database.users import users
from fastapi_demo.database.animals import animals

# Models
from fastapi_demo.models.models import User, Tags

# Dependencies
from fastapi_demo.dependencies.pagination import paginate
from fastapi_demo.dependencies.resources import ValidUserDep, ValidAnimalDep

app = FastAPI()

@app.get("/", tags=[Tags.home], summary='Simple Hello World message')
async def hello_world():
    return { "message": "Hello World!" }

# -----------------------------
# ----------- USERS -----------
# -----------------------------
@app.get('/users', tags=[Tags.users], summary='List of users with pagination and search by name')
async def get_users(page: Annotated[dict, Depends(paginate(users))]):
    return page

@app.get('/users/{item_id}', status_code=status.HTTP_200_OK, tags=[Tags.users])
async def get_user_by_id(user: ValidUserDep):
    return {
        "status": status.HTTP_200_OK, 
        "data": user
    }

@app.post('/users', tags=[Tags.users], response_description="User created successfully!")
async def create_user(user: User):
    return {
        "message": f"User {user.name} with ID {user.id} created successfully!"
    }

# -----------------------------
# ---------- ANIMALS ----------
# -----------------------------
@app.get('/animals', tags=[Tags.animals])
async def get_animals(page: Annotated[dict, Depends(paginate(animals))]):
    return page

@app.get('/animals/{item_id}', status_code=status.HTTP_200_OK, tags=[Tags.animals])
async def get_animal_by_id(animal: ValidAnimalDep):
    return {
        "status": status.HTTP_200_OK, 
        "data": animal
    }