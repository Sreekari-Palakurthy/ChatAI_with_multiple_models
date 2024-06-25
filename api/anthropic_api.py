import os
import requests
import json

def validate_anthropic_key() -> bool:
    url = "https://api.anthropic.com/v1/complete"
    payload = json.dumps({
        "model": "claude-2.1",
        "max_tokens_to_sample": 1024,
        "prompt": "\n\nHuman: Hello, Claude\n\nAssistant:"
    })
    headers = {
        'x-api-key': os.getenv('ANTHROPIC_API_KEY'),
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code == 200
