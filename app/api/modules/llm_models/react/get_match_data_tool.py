from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from statsbombpy import sb

class Input(BaseModel):
    match_id: int = Field(description="should the id of the analysed match")


@tool("get-match-data", args_schema=Input, return_direct=True)
def get_match_data(match_id: int) -> str:
    """Get the match events data in json format"""
    try:
        match_events = sb.events(match_id=match_id)
        match_events_json = match_events.to_dict(orient="records")
        return str(match_events_json)
    except Exception as e:
        return f"Não foi possível encontrar os eventos da partida {match_id}"