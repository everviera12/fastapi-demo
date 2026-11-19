from typing import Annotated
from fastapi import Depends, Header, HTTPException, status

def verify_api_key(x_api_key: Annotated[str | None, Header()] = None) -> str:
    if x_api_key != 'secret-api-key':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key is invalid"
        )
    return x_api_key


def require_admin(api_key: Annotated[str, Depends(verify_api_key)], x_role: Annotated[str | None, Header()] = "guest") -> str:
    print(api_key)
    if x_role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for non-admin users"
        )
    return x_role