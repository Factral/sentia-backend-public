import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import GoogleV3

'''
# Cargar el dataset
data = pd.read_csv("/media/manuela/Mis archivos/ProyectoU24/Datos/_DatosUnidades.csv")

# Crear una instancia del geocodificador Nominatim
geolocator = Nominatim(user_agent="mi_aplicacion")

# Función para obtener la dirección a partir del nombre del lugar
def obtener_direccion(nombre_lugar):
    try:
        location = geolocator.geocode(nombre_lugar + ", Bucaramanga")
        if location:
            return location.address
        else:
            return "Dirección no encontrada"
    except:
        return "Error de conexión"

# Aplicar la función a la columna de nombres de lugares y almacenar en una nueva columna
data['direccion'] = data['nom_upgd'].apply(lambda x: obtener_direccion(x))
sleep(1)  # Espera para cumplir con los límites de la API

# Guardar el DataFrame actualizado con las direcciones
data.to_csv("lugares_con_direcciones.csv", index=False)
print("Proceso completado. Las direcciones se guardaron en 'lugares_con_direcciones.csv'.")
'''

data = pd.read_csv('/media/manuela/Mis archivos/ProyectoU24/lugares_con_direcciones.csv')

print(data.columns)

data.columns = data.columns.str.strip()

data1 = data[data['direccion'] != 'Dirección no encontrada']
print(data1)
#------------------------------------------------------------------------------------------

geolocator = Nominatim(user_agent="myGeocoder")

def obtener_coordenadas(direccion):
    try:
        location = geolocator.geocode(direccion)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error al geocodificar {direccion}: {e}")
        return None, None

data1[['latitud', 'longitud']] = data1['direccion'].apply(lambda x: pd.Series(obtener_coordenadas(x)))

print(data1)

data1.to_csv('/media/manuela/Mis archivos/ProyectoU24/Datos/_DatosUnidades_con_coordenadas.csv', index=False)

def generar_mapa_html(df):
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Mapa de Centros de Salud</title>
        <script src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY" defer></script>
        <script defer>
          function initMap() {
            const center = { lat: 7.119349, lng: -73.122741 };  // Ubicación central en Bucaramanga
            const map = new google.maps.Map(document.getElementById("map"), {
              zoom: 13,
              center: center,
            });

            const centrosSalud = [
    """

    for _, row in df.dropna(subset=['latitud', 'longitud']).iterrows():
        html += f"{{ lat: {row['latitud']}, lng: {row['longitud']}, name: '{row['nom_upgd']}' }},\n"

    html += """
            ];

            centrosSalud.forEach((centro) => {
              new google.maps.Marker({
                position: { lat: centro.lat, lng: centro.lng },
                map,
                title: centro.name,
              });
            });
          }
        </script>
      </head>
      <body onload="initMap()">
        <div id="map" style="height: 100%; width: 100%;"></div>
      </body>
    </html>
    """
    
    with open("/media/manuela/Mis archivos/ProyectoU24/Mapa_centros_salud.html", "w") as file:
        file.write(html)

generar_mapa_html(data1)