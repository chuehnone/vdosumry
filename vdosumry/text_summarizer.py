import json
import requests

class TextSummarizer:
    def __init__(self, model):
        self.model = model

    def summarize(self, text: str) -> str:
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "prompt": f"請將以下逐字稿內容整理成摘要：\n\n{text}",
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
            raise Exception(f"摘要生成失敗：{response.status_code} - {response.text}")