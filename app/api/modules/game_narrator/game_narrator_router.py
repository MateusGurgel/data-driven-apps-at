from fastapi import APIRouter

from api.modules.llm_models.gemini import Gemini

from api.modules.game_narrator.game_narrator_dto import CreateGameNarrativeDTO, GameNarrativeDTO

from api.modules.game_narrator.game_narrator_command import GameNarratorCommand

game_narrator_router = APIRouter()

@game_narrator_router.post("/game_narrator")
async def game_narrator(create_player_profile: CreateGameNarrativeDTO) -> GameNarrativeDTO:
    model = Gemini()
    game_narrator_command = GameNarratorCommand(model)
    return game_narrator_command.execute(create_player_profile)