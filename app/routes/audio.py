from fastapi import APIRouter, Request, HTTPException, File, UploadFile, Form
from pydantic import BaseModel

import os

import json
from groq import Groq
from huggingface_hub.inference_api import InferenceApi

from ..LLM.gemini import model_identify_variables, model_sentia
from ..LLM.hf import query, PARAMETERS_HF
from ..utils.utils import extract_json
from ..utils.predict_mechanism import predict_mechanism
from ..utils.prompts import PROMPT_SENTIA

client = Groq(
    api_key="PUT-YOUR-API-KEY-HERE"
)

audio_route = APIRouter()

SAVE_DIRECTORY = "uploaded_audios"
os.makedirs(SAVE_DIRECTORY, exist_ok=True)


@audio_route.post('/upload-audio')
async def upload_audio(file: UploadFile = File(...),     name: str = Form(...) ):
    """
    Endpoint to upload audio files and save them to a folder.
    """
    file_path = os.path.join(SAVE_DIRECTORY, file.filename)

    with open(file_path, "wb") as audio_file:
        audio_file.write(await file.read())

    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(file_path, file.read()),
        model="whisper-large-v3",
        prompt="a spanish person talking about their life, transcript in spanish language.",  
        response_format="json",
        language="es",
        temperature=0.0  
        )

    os.remove(file_path)    

    response_model = model_identify_variables.generate_content(
        transcription.text
    )

    try:
        parsed_response = extract_json(response_model.text)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Response model is not a valid JSON")

    parsed_response["sexo_"]  = "M"
    parsed_response["edad_"] = 25
    parsed_response["area_"] = 1
    parsed_response["prob_consu"] = 1

    # predicted mechanism
    predicted_mechanis = predict_mechanism(parsed_response)

    output_sentiment = query({
        "inputs": transcription.text,
        "parameters": PARAMETERS_HF
    })

    # analyzed sentiments
    sentiment_text1, sentiment_text2 = output_sentiment["labels"][0], output_sentiment["labels"][1]

    #make inference with sentia
    response_sentia = model_sentia.generate_content(
        PROMPT_SENTIA.format(
            transcription=transcription.text,
            mechanism=predicted_mechanis,
            emotion1=sentiment_text1,
            emotion2=sentiment_text2
        )
    )


    return {"message": "Audio file uploaded successfully",
                "file_path": file_path,
                "transcription": response_sentia.text,
                "response_model": parsed_response,
                "name": name
                }
