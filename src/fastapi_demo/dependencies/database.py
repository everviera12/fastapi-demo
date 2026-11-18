from fastapi import HTTPException, Depends
from typing import Annotated

from fastapi_demo.database.users import users
from fastapi_demo.database.animals import animals

class InternalError(Exception):
    pass

def get_db():
    print("Open database...")

    try:
        print("Databse conected successfuly")
        yield {
            "users": users,
            "animals": animals
        }

    except InternalError as e:
        print("Error trying to connect to the database")
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")

    finally:
        print("Database closed successfully")

DBDep = Annotated[dict, Depends(get_db)]