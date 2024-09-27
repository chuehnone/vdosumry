from .llm.base import LlmBase


class TextSummarizer:
    def __init__(self, llm: LlmBase):
        self.llm = llm

    def summarize(self, text: str) -> str:
        prompt = f"請將以下逐字稿內容整理成摘要：\n\n{text}"
        try:
            return self.llm.generate(prompt)
        except Exception as e:
            raise Exception(f"摘要生成失敗：{e}")
