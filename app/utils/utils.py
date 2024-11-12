import json
import re


def extract_json(response):
    json_data = {}
    json_match = re.search(r'\{.*\}', response, re.DOTALL)

    if json_match:
        json_text = json_match.group(0)
        json_data = json.loads(json_text)
    else:
        print("No se encontró un JSON válido en el texto.")

    return json_data