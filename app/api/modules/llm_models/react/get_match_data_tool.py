from langchain_core.tools import tool
from statsbombpy import sb

@tool
def get_match_data(match_id: int) -> str:
    """
        Retrieves and filters match event data from the Statsbomb API.

        This function fetches match events data and filters for relevant events including:
        - Shots with outcomes
        - Fouls resulting in cards
        - Passes that resulted in assists

        Args:
            match_id (int): The unique identifier of the match to retrieve data for

        Returns:
            str: A string representation of the filtered match events in JSON format.
                Contains details like shot outcomes, team info, player data, and timestamps.
                If an error occurs, returns an error message with the match_id.

        Raises:
            No exceptions are raised - errors are caught and returned as error messages

        Example:
            >> match_data = get_match_data(3869685)
            >> print(match_data)  # Returns JSON string of match events or error message
    """

    try:
        events = sb.events(match_id=int(match_id))
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
        match_events_json = relevant_events.to_dict(orient="records")
        return str(match_events_json)
    except Exception as e:
        return f"Não foi possível encontrar os eventos da partida {match_id}"