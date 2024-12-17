from pydantic import BaseModel

class GetAgentResponseDTO(BaseModel):
    match_id: int
    question: str

class AgentResponseDTO(BaseModel):
    summary: str