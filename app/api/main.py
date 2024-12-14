from fastapi import FastAPI

from .modules.game_narrator.game_narrator_router import game_narrator_router
from .modules.match_summarizer.match_summarizer_router import match_summarizer_router
from .modules.player_profiler.player_profiler_router import player_profiler_router

app = FastAPI()

# Application Routes
app.include_router(match_summarizer_router)
app.include_router(player_profiler_router)
app.include_router(game_narrator_router)