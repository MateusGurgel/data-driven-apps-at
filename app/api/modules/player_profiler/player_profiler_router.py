from fastapi import APIRouter

from api.modules.player_profiler.player_profiler_dto import CreatePlayerProfileDTO, PlayerProfileDTO

from api.modules.llm_models.gemini import Gemini

from api.modules.player_profiler.player_profiler_command import PlayerProfilerCommand

player_profiler_router = APIRouter()

@player_profiler_router.post("/profile")
async def profile_player(create_player_profile: CreatePlayerProfileDTO) -> PlayerProfileDTO:
    model = Gemini()
    player_profiler_command = PlayerProfilerCommand(model)
    return player_profiler_command.execute(create_player_profile)