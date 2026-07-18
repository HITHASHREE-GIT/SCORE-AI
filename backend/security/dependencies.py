from fastapi import Depends, HTTPException

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from backend.security.jwt import verify_token



security = HTTPBearer()



def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials


    payload = verify_token(token)


    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


    return {

        "id": int(payload["sub"]),

        "email": payload.get("email")

    }