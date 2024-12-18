from langchain_core.tools import tool
from statsbombpy import sb

@tool
def get_passes(match_id: int) -> str:
    """
        Retrieves and counts passes per player for a specific match.

        This function uses StatsBombPy to extract match events and group passes
        by player, returning a JSON string with the results.

        Parameters
        ----------
        match_id : int
            The unique identifier of the match in the StatsBomb dataset.

        Returns
        -------
        str
            A JSON string containing a list of dictionaries with:
            - player_id: Player identifier
            - player: Player name
            - count: Total number of passes by the player in the match

        Exceptions
        ----------
        Returns an error message if unable to retrieve match events.

        Example
        -------
        >>> passes = get_passes(12345)
        >>> print(passes)
        # Output: JSON with players' pass statistics
    """

    try:
        events = sb.events(match_id=int(match_id))

        # Group by player and count passes by player, the output should be with player name
        passes = events.groupby(["player_id", "player"])["play_pattern"].count().reset_index()
        passes = passes.rename(columns={"play_pattern": "count"})

        # Convert to JSON string to ensure serialization
        passes_json = passes.to_json(orient="records")
        return str(passes_json)
    except Exception as e:
        return f"Não foi possível encontrar os eventos da partida {match_id}"