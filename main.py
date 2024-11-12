from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    auth_route,
    ping_route,
    text_route,
    audio_route,
    update_history_route
    )

app = FastAPI(
    title="sentIA Backend",
    description="Datos a la U",
    version="0.0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_route)
app.include_router(ping_route)
app.include_router(text_route)
app.include_router(audio_route)
app.include_router(update_history_route)