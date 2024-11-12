from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

classify_feelings_route = APIRouter()

class ClassifyFeelings(BaseModel):
    text: str

@classify_feelings_route.post('/classify_feelings')
async def classify_feelings(request: Request):
    data = request.json()
    text_input = data.get("text")

    if text_input is None:
        raise HTTPException(status_code=400, detail="No text input provided")

    try:
        pass

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))