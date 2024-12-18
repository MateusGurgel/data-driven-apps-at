import json

import google.generativeai as genai
from decouple import config
from modules.llm_models.llm_interface import LlmModel

genai.configure(api_key=config("GEMINI_TOKEN"))

class Gemini(LlmModel):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        pass

    def generate_text(self, text: str) -> str:
        return self.model.generate_content(text).text

    def generate_text_with_json_response(self, text: str) -> dict:
        response_text = self.model.generate_content(text, generation_config=genai.GenerationConfig(response_mime_type="application/json")).text
        json_response = json.loads(response_text)
        return json_response