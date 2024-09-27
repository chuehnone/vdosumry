import json
import requests
from .base import LlmBase


class Ollama(LlmBase):
    def __init__(self, model, uri="http://localhost:11434/api/generate"):
        self.model = model
        self.uri = uri

    def generate(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "prompt": prompt,
        }
        response = requests.post(self.uri, headers=headers, json=data)
        if response.status_code == 200:
            data = "".join(
                json.loads(line)["response"]
                for line in response.text.splitlines()
                if line.strip()
            )
            return data
        else:
            raise Exception(f"{response.status_code} - {response.text}")
