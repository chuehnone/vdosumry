import json
import requests
from .base import LlmBase


class Ollama(LlmBase):
    def __init__(self, model: str, uri: str = "http://localhost:11434/api/generate"):
        self.model = model
        self.uri = uri

    def generate(self, prompt: str) -> str:
        """
        Generate text based on the prompt.
        :param prompt:
        :return:
        :exception RuntimeError:
        :exception ValueError:
        """

        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "prompt": prompt,
        }
        try:
            response = requests.post(self.uri, headers=headers, json=data)
            response.raise_for_status()
            return self._parse_response(response.text)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    @staticmethod
    def _parse_response(response_text: str) -> str:
        try:
            data = "".join(
                json.loads(line)["response"]
                for line in response_text.splitlines()
                if line.strip()
            )
            return data
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to parse response: {e}")
