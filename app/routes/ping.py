from fastapi import APIRouter, Request, HTTPException
from app.services.firebase import firebase
from pydantic import BaseModel

ping_route = APIRouter()


class FirebaseUser(BaseModel):
    email: str
    password: str


@ping_route.post('/ping')
async def login(request: Request):
    """
    test login
    """
    headers = request.headers
    jwt = headers['Authorization']
    try:
        user = firebase.auth().get_account_info(jwt)
        return {"user": user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))