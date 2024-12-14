from fastapi import HTTPException
from statsbombpy import sb

from api.modules.llm_models.llm_interface import LlmModel

from api.modules.player_profiler.player_profiler_dto import CreatePlayerProfileDTO, PlayerProfileDTO


class PlayerProfilerCommand:
    def __init__(self, model: LlmModel):
        self.model = model

    def execute(self, create_match_summary: CreatePlayerProfileDTO) -> PlayerProfileDTO:
        try:
            events = sb.events(match_id=create_match_summary.match_id)
        except Exception as e:
            raise HTTPException(status_code=404, detail="Não foi possível encontrar os eventos da partida")

        # Filtering relevant events

        relevant_events = events[events["player_id"] == create_match_summary.player_id]
        relevant_events = relevant_events[relevant_events["shot_outcome"].notna() | relevant_events["foul_committed_card"] | relevant_events["pass_goal_assist"].notna()]
        relevant_events = relevant_events[
            [
                "shot_outcome",
                "under_pressure",
                "team",
                "tactics",
                "shot_type",
                "shot_technique",
                "player",
                "play_pattern",
                "timestamp",
                "period",
                "foul_committed_card",
                "pass_goal_assist"
            ]
        ]

        # Transforming the data into json format

        relevant_events_json = relevant_events.to_dict(orient="records")

        prompt = f"""
        You are a professional football summarizer. 
        Your task is to summarize the events and performance of a player on a match in a concise and informative manner. 
        Please provide a comprehensive summary of the match, including key statistics, highlights, and insights.
        
        1. The Response should be in Portuguese.
        2. The Response should be in a clear and concise manner, avoiding jargon and technical terms.
        3. Be sure that even if the reader does not understand about soccer, they can understand the main points of the match.
        
        <match_events>
        {relevant_events_json}
        </match_events>
        """

        summary = self.model.generate_text(prompt)

        return PlayerProfileDTO(summary=summary, events=relevant_events_json)
