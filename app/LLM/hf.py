import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": "Bearer PUT-YOUR-API-KEY-HERE"}

PARAMETERS_HF = {"candidate_labels": 
["Calm","Anxiety","Sadness", "Irritation", "Hopeful", "Overwhelmed", "Loneliness", "Contentment","Anger","Fear"]}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


