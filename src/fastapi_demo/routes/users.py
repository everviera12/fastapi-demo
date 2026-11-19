from fastapi import APIRouter, Depends, status
from typing import Annotated

from fastapi_demo.database.users import users
from fastapi_demo.models.models import User, Tags
from fastapi_demo.dependencies.auth import verify_api_key, require_admin
from fastapi_demo.dependencies.pagination import paginate
from fastapi_demo.dependencies.resources import ValidUserDep

router = APIRouter(
    prefix="/users",
    tags=[Tags.users],
    dependencies=[Depends(verify_api_key)]
)

@router.get('', tags=[Tags.users], summary='List of users with pagination and search by name')
async def get_users(page: Annotated[dict, Depends(paginate(users))]):
    return page

@router.get('/{item_id}', status_code=status.HTTP_200_OK, tags=[Tags.users])
async def get_user_by_id(user: ValidUserDep):
    return {
        "status": status.HTTP_200_OK, 
        "data": user
    }

@router.post('', tags=[Tags.users], dependencies=[Depends(require_admin)], response_description="User created successfully!")
async def create_user(user: User) -> dict:
    return {
        "message": f"User {user.name} with ID {user.id} created successfully!"
    }