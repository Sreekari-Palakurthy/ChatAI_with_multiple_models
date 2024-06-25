import os
from openai import OpenAI
from typing import List

def get_openai_models() -> List[str]:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.models.list()
    model_names = [model['id'] for model in response['data']]
    return model_names
