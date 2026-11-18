from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

# Database simulation
from fastapi_demo.database.users import users
from fastapi_demo.database.animals import animals

# Models
from fastapi_demo.models.models import User, Tags

# Dependencies
from fastapi_demo.dependencies.pagination import paginate

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

@app.get('/users/{user_id}', status_code=status.HTTP_200_OK, tags=[Tags.users])
async def get_users_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {
                "status": status.HTTP_200_OK,
                "message": "User founded successfully!",
                "data": user
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

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

@app.get('/animals/{animal_id}', status_code=status.HTTP_200_OK, tags=[Tags.animals])
async def get_animal_by_id(animal_id: int):
    for animal in animals:
        if animal["id"] == animal_id:
            return {
                "status": status.HTTP_200_OK,
                "data": animal
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Animal not found"
    )