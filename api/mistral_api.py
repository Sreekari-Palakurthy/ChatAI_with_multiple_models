import os
import requests
from typing import List

def get_mistral_models() -> List[str]:
    url = "https://api.mistral.com/v1/models"  # Replace with the actual endpoint
    headers = {
        'Authorization': f'Bearer {os.getenv("MISTRAL_API_KEY")}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        model_names = [model['name'] for model in data['models']]  # Adjust based on actual response structure
        return model_names
    else:
        response.raise_for_status()
