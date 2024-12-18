from typing import List

from pydantic import BaseModel

class CreatePlayerProfileDTO(BaseModel):
    player_id: int
    match_id: int

class PlayerProfileDTO(BaseModel):
    summary: str
    events: List[dict]