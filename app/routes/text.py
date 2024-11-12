import os
import google.generativeai as genai
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

# Configure the Gemini API
genai.configure(api_key="PUT-YOUR-API-KEY-HERE")

text_route = APIRouter()

# class FirebaseUser(BaseModel):
#     text: str

@text_route.post('/process')
async def process_text(request: Request):
    data = await request.json()
    text_input = data.get("text")

    if text_input is None:
        raise HTTPException(status_code=400, detail="No text input provided")

    # Choose Gemini model (gemini-pro, gemini-1.5-flash)
    model = genai.GenerativeModel("gemini-pro")

    try:
        # Generate a response from Gemini
        response = model.generate_content(
            text_input,
        )
        return {"gemini_response": response.text}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))