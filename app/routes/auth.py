from fastapi import APIRouter, Form, HTTPException
from app.services.firebase import firebase
from pydantic import BaseModel

auth_route = APIRouter()


class FirebaseUser(BaseModel):
    email: str
    password: str


@auth_route.post('/login')
async def login(request: FirebaseUser):
    """
    Login endpoint for users
    """
    email = request.email
    password = request.password
   
    if email is None or password is None:
        raise HTTPException(status_code=400, detail="Email or password is missing")
   
    try:
        user = firebase.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {"token": jwt}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
      