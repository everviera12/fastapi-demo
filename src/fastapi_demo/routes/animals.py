from fastapi import APIRouter, Depends, status
from typing import Annotated

from fastapi_demo.database.animals import animals
from fastapi_demo.models.models import Tags
from fastapi_demo.dependencies.auth import verify_api_key
from fastapi_demo.dependencies.pagination import paginate
from fastapi_demo.dependencies.resources import ValidAnimalDep

router = APIRouter(
    prefix="/animals",
    tags=[Tags.animals],
    dependencies=[Depends(verify_api_key)]
)

@router.get("")
async def get_animals(page: Annotated[dict, Depends(paginate(animals))]) -> dict:
    return page

@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_animal_by_id(animal: ValidAnimalDep) -> dict:
    return {
        "status": status.HTTP_200_OK, 
        "data": animal
    }