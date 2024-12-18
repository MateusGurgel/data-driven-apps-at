from typing import List, Literal

from pydantic import BaseModel

class CreateGameNarrativeDTO(BaseModel):
    match_id: int
    narrative_style: Literal["Formal", "Humorist", "Technical"]

class GameNarrativeDTO(BaseModel):
    narration: str