import json
import requests
from .base import LlmBase


class Ollama(LlmBase):
    def __init__(self, uri: str = "http://localhost:11434"):
        self.model = None
        self.uri = uri

    def set_default_model(self, model: str) -> None:
        self.model = model

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

        generate_uri = self.uri + "/api/generate"
        try:
            response = requests.post(generate_uri, headers=headers, json=data)
            response.raise_for_status()
            return self.__parse_generate_json_lines_response(response.text)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    def list(self) -> list[str]:
        """
        List available models.
        :return:
        :exception RuntimeError:
        :exception ValueError:
        """

        list_uri = self.uri + "/api/tags"
        try:
            response = requests.get(list_uri)
            response.raise_for_status()
            return [model["model"] for model in json.loads(response.text)["models"]]
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    @staticmethod
    def __parse_generate_json_lines_response(response_text: str) -> str:
        try:
            data = "".join(
                json.loads(line)["response"]
                for line in response_text.splitlines()
                if line.strip()
            )
            return data
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to parse response: {e}")
