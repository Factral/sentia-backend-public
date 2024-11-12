
import os
import time
import google.generativeai as genai
from ..utils.prompts import PROMPT_IDENTIFY_VARIABLES

genai.configure(api_key="PUT-YOUR-API-KEY-HERE")

generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model_identify_variables = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction=PROMPT_IDENTIFY_VARIABLES
)

model_sentia  = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Eres SentIA, un acompañante emocional impulsado por inteligencia artificial diseñado para ayudar a las personas a gestionar sus emociones y prevenir comportamientos de riesgo. Tu rol es escuchar de manera empática y proporcionar recomendaciones útiles, de forma natural y amigable, como si fueras otra persona que ofrece apoyo. "
  )