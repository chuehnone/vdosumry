from .llm.base import LlmBase


class TextTranslator:
    def __init__(self, target_language, llm: LlmBase):
        self.target_language = target_language
        self.llm = llm

    def translate(self, text: str) -> str:
        prompt = f"請將以下內容翻譯成 {self.target_language} 的語言： \n\n{text}"
        try:
            return self.llm.generate(prompt)
        except Exception as e:
            raise Exception(f"翻譯失敗：{e}")
