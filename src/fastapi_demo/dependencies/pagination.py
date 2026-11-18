import math
from fastapi import Query, Depends
from typing import Annotated, Any

# Models
from fastapi_demo.models.models import Pagination

def paginate(items: list[dict[str, Any]]):
    async def paginated(
        pagination: Annotated[Pagination, Depends()],
        search: Annotated[str | None, Query(description="Search by name")] = None
    ) -> dict:

        
        results = items.copy()
        if search:
            results = [
                i for i in results
                if search.lower() in i["name"].lower()
            ]

        total_count = len(results)
        total_pages = math.ceil(total_count / pagination.size) if total_count else 0
        start = (pagination.page - 1) * pagination.size

        return {
            "metadata": {
                "total_matches": total_count,
                "total_pages": total_pages,
                "current_page": pagination.page,
                "page_size": pagination.size,
                "search_term": search,
                "next_page": pagination.page + 1 if pagination.page < total_pages else None,
                "prev_page": pagination.page - 1 if pagination.page > 1 else None,
            },
            "data": results[start : start + pagination.size],
        }
    
    return paginated