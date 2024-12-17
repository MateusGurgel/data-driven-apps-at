from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from statsbombpy import sb

class Input(BaseModel):
    match_id: str = Field(description="should the id of the analysed match")
    player_id: str = Field(description="Should be the id of a specific player on the match")

@tool("get-player-data", args_schema=Input, return_direct=True)
def get_player_data(player_id: str, match_id: str) -> str:
    """Get the player events in a match in json format"""
    try:
        events = sb.events(match_id=match_id)
        events = events[events["player_id"] == player_id]
        events_json = events.to_dict(orient="records")
        return str(events_json)
    except Exception as e:
        return f"Não foi possível encontrar os eventos do jogador {player_id} na partida {match_id}"