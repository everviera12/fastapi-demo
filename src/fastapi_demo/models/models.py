from enum import Enum
from fastapi import Query
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str

class Pagination(BaseModel):
    page: int = Field(1, ge=1, description="Page number (Starts in 1th)")
    size: int = Field(5, ge=1, le=100, description="Elements per page")

class Filters(BaseModel):
    tags: list[str] = Query(default=[])

class Tags(Enum):
    home = "Hello World message"
    users = "Users"
    animals = "Animals"