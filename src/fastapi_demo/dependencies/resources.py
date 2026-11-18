from typing import Annotated
from fastapi import Depends, HTTPException, status

from fastapi_demo.dependencies.database import DBDep

def get_by_id(collection: str, entity_name: str):
    def dependency(item_id: int, db: DBDep) -> dict:
        for item in db[collection]:
            if item["id"] == item_id:
                return {
                    "status": status.HTTP_200_OK,
                    "data": item
                }
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{entity_name} not found"
        )

    return dependency

ValidUserDep = Annotated[dict, Depends(get_by_id("users", "User"))]
ValidAnimalDep = Annotated[dict, Depends(get_by_id("animals", "Animal"))]