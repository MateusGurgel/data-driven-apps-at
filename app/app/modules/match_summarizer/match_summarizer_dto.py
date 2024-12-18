from pydantic import BaseModel

class CreateMatchSummaryDTO(BaseModel):
    match_id: int

class MatchSummaryDTO(BaseModel):
    summary: str