from fastapi import APIRouter

from api.modules.react_agent.react_agent_command import ReactAgentCommand
from api.modules.react_agent.react_agent_dto import GetAgentResponseDTO, AgentResponseDTO

from api.modules.llm_models.react.react import ReactAgent

react_agent_router = APIRouter()

@react_agent_router.post("/react")
async def react_agent_route(agent_response: GetAgentResponseDTO) -> AgentResponseDTO:
    model = ReactAgent()
    react_agent = ReactAgentCommand(model)
    return react_agent.execute(agent_response)