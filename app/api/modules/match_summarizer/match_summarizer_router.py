from fastapi import APIRouter

from .match_summarizer_command import MatchSummaryCommand
from .match_summarizer_dto import CreateMatchSummaryDTO, MatchSummaryDTO
from ..llm_models.gemini import Gemini

match_summarizer_router = APIRouter()

@match_summarizer_router.post("/summarize")
async def summarize_match(match_summary_dto: CreateMatchSummaryDTO) -> MatchSummaryDTO:
    model = Gemini()
    match_summary_command = MatchSummaryCommand(model)
    return match_summary_command.execute(match_summary_dto)