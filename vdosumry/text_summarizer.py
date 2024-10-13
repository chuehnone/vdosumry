from .llm.base import LlmBase


class TextSummarizer:
    def __init__(self, llm: LlmBase):
        self.llm = llm

    def summarize(self, text: str) -> str:
        prompt = f"""
# 整理逐字稿內容

## 需求
- 將內容拆分成多個段落
  - 每個段落有代表主題
  - 每個段落會有多個問題與答案

## 逐字稿內容
{text}
"""
        try:
            return self.llm.generate(prompt)
        except Exception as e:
            raise Exception(f"摘要生成失敗：{e}")
