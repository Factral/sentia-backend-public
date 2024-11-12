from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from app.services.firebase import db
from pydantic import BaseModel

update_history_route = APIRouter()

class HistoryUpdate(BaseModel):
    username: str
    data: dict

@update_history_route.post("/update-history")
def update_user_history(history_update: HistoryUpdate = Body(...)):
    """
    Actualiza el historial de un usuario en la base de datos de Firebase.

    Parámetros:
    history_update (HistoryUpdate): Un objeto que contiene el nombre de usuario y los datos a actualizar.

    Retorna:
    dict: Un diccionario que confirma que la actualización se realizó correctamente.
    """
    username = history_update.username
    data = history_update.data

    # Actualizar el historial del usuario en la base de datos de Firebase
    db.child(username).set(data)

    return {"message": "Historial actualizado correctamente."}



@update_history_route.get("/get-history/{username}")
def get_user_history(username: str):
    """
    Obtiene el historial de un usuario de la base de datos de Firebase.

    Parámetros:
    username (str): El nombre de usuario cuya información se desea obtener.

    Retorna:
    dict: Un diccionario con los datos del historial del usuario.
    """
    try:
        # Obtener el historial del usuario desde la base de datos de Firebase
        user_history = db.child(username).get().val()
        
        if user_history is None:
            raise HTTPException(status_code=404, detail="Historial no encontrado para el usuario especificado.")
        
        return {"username": username, "history": user_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el historial del usuario: {e}")


class HistoryEntry(BaseModel):
    username: str
    date: str
    transcript: str
    sentiment: str


@update_history_route.post("/add-history")
def add_user_history(entry: HistoryEntry = Body(...)):
    """
    Agrega una entrada al historial de un usuario en la base de datos de Firebase.

    Parámetros:
    entry (HistoryEntry): Un objeto que contiene el nombre de usuario, la fecha, el transcript y el sentimiento de la entrada.

    Retorna:
    dict: Un diccionario que confirma que la entrada fue añadida correctamente.
    """
    username = entry.username

    try:
        # Obtener el historial actual del usuario
        current_history = db.child(username).child("history").get().val() or []

        # Crear la nueva entrada y agregarla al historial
        new_entry = {
            "date": entry.date,
            "transcript": entry.transcript,
            "sentiment": entry.sentiment
        }
        current_history.append(new_entry)

        # Guardar el historial actualizado en Firebase
        db.child(username).child("history").set(current_history)

        return {"message": "Entrada añadida correctamente al historial."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al añadir la entrada al historial: {e}")