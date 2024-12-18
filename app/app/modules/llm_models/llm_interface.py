from abc import ABC, abstractmethod

class LlmModel(ABC):
    @abstractmethod
    def generate_text(self, text: str) -> str:
        pass

    @abstractmethod
    def generate_text_with_json_response(self, text: str) -> dict:
        pass