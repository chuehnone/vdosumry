import json
import requests

class TextTranslator:
    def __init__(self, target_language, model):
        self.target_language = target_language
        self.model = model

    def translate(self, text: str) -> str:
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "prompt": f"請將以下內容翻譯成 {self.target_language} 的語言： ```\n\n{text}```",
        }
        response = requests.post(
            "http://localhost:11434/api/generate", headers=headers, json=data
        )
        if response.status_code == 200:
            data = "".join(
                json.loads(line)["response"]
                for line in response.text.splitlines()
                if line.strip()
            )
            return data
        else:
            raise Exception(f"翻譯失敗: {response.status_code} - {response.text}")