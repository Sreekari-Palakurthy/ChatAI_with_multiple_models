import requests
import json
from typing import List
from openai import OpenAI
import os

def validate_anthropic_key() -> bool:
    url = "https://api.anthropic.com/v1/complete"
    payload = json.dumps({
    "model": "claude-2.1",
    "max_tokens_to_sample": 1024,
    "prompt": "\n\nHuman: Hello, Claude\n\nAssistant:"
    })
    headers = {
    'x-api-key': '$ANTHROPIC_API_KEY',
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def get_openai_models() -> List[str]:
    client = OpenAI(
        api_key = os.getenv('OPENAI_API_KEY')
    )
    models = client.models.list()
    print(models)


def get_mistral_models() -> List[str]:
    url = "https://api.mistral.com/v1/models"  # Replace with the actual endpoint

    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise EnvironmentError("MISTRAL_API_KEY environment variable not set")

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        models = data.get('models', [])
        
        if not models:
            raise ValueError("No models found in the response")
        
        model_names = []
        for model in models:
            name = model.get('name')
            if name is None:
                raise ValueError(f"Model without a name found: {model}")
            model_names.append(name)
        
        return model_names
    else:
        response.raise_for_status()

