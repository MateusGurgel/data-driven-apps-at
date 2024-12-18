from langchain_core.tools import tool
from statsbombpy import sb
import json

@tool
def get_specific_player_data(query) -> str:
    """
    Retrieves all events associated with a specific player in a match from Statsbomb API.

    This function fetches and filters match events data for a specific player,
    providing a comprehensive view of the player's actions during a match.

    Args:
        query (dict): A dictionary containing two key-value pairs:
            - 'player_id' (int): The unique identifier of the player
            - 'match_id' (int): The unique identifier of the match

    Returns:
        str: A JSON-formatted string containing all events involving the specified player.
             The events are extracted from the match data and filtered by player ID.

    Raises:
        ValueError: If the player ID or match ID cannot be converted to integers
        Exception: If there are issues retrieving or processing the match events

    Example:
        >>> result = get_specific_player_data({
        ...     "player_id": 40724,
        ...     "match_id": 3895302
        ... })
        >>> print(result)  # Outputs JSON string of player events
    """
    try:
        # Ensure inputs are integers
        player_id = int(query["player_id"])
        match_id = int(query["match_id"])

        # Fetch events for the specific match
        events = sb.events(match_id=match_id)

        relevant_events = events[
            [
                "shot_outcome",
                "team",
                "shot_type",
                "shot_technique",
                "player",
                "player_id",
                "play_pattern",
                "timestamp",
                "period",
                "foul_committed_card",
                "pass_goal_assist"
            ]
        ]

        # Filter events for the specific player
        player_events = relevant_events[relevant_events["player_id"] == player_id]

        # Convert to JSON string to ensure serialization
        events_json = json.dumps(player_events.to_dict(orient="records"), ensure_ascii=False)

        return events_json
    except ValueError:
        return f"Erro: IDs inválidos - player_id: {query.get('player_id')}, match_id: {query.get('match_id')}"
    except Exception as e:
        return f"Não foi possível encontrar os eventos do jogador {query.get('player_id')} na partida {query.get('match_id')}. Erro: {str(e)}"