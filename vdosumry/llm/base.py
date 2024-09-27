from abc import ABC, abstractmethod


class LlmBase(ABC):
    @abstractmethod
    def generate(self, text: str) -> str:
        pass
