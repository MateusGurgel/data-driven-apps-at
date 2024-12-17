from fastapi import HTTPException
from statsbombpy import sb

from api.modules.llm_models.llm_interface import LlmModel

from api.modules.react_agent.react_agent_dto import GetAgentResponseDTO, AgentResponseDTO


class ReactAgentCommand:
    def __init__(self, model: LlmModel):
        self.model = model

    def execute(self, create_match_summary: GetAgentResponseDTO) -> AgentResponseDTO:
        summary = self.model.generate_text(f"Pergunta: {create_match_summary.question} Id da partida: {create_match_summary.match_id}")
        return AgentResponseDTO(summary=summary)
