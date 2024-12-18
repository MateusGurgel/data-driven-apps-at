from fastapi import HTTPException

from modules.llm_models.llm_interface import LlmModel

from modules.react_agent.react_agent_dto import GetAgentResponseDTO, AgentResponseDTO


class ReactAgentCommand:
    def __init__(self, model: LlmModel):
        self.model = model

    def execute(self, create_match_summary: GetAgentResponseDTO) -> AgentResponseDTO:
        try:
            summary = self.model.generate_text(f"Pergunta: {create_match_summary.question} Id da partida: {create_match_summary.match_id}")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Não foi possível gerar a resposta")
        return AgentResponseDTO(summary=summary)
