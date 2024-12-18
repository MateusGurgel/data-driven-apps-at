from statsbombpy import sb

from modules.game_narrator.game_narrator_dto import GameNarrativeDTO
from modules.game_narrator.game_narrator_dto import CreateGameNarrativeDTO
from modules.llm_models.llm_interface import LlmModel


class GameNarratorCommand:
    def __init__(self, model: LlmModel):
        self.model = model

    def execute(self, create_game_narrative: CreateGameNarrativeDTO) -> GameNarrativeDTO:
        try:
            events = sb.events(match_id=create_game_narrative.match_id)
        except Exception as e:
            raise HTTPException(status_code=404, detail="Não foi possível encontrar os eventos da partida")

        # Filtering relevant events

        relevant_events = events[events["shot_outcome"].notna() | events["foul_committed_card"] | events["pass_goal_assist"].notna()]
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
        You are a professional football narrator. 
        Your task is to narrate the events of a match in a concise and informative manner and in cronological order.
        
        1. The Response should be in Portuguese.
        2. Use the narrative should be on a {create_game_narrative.narrative_style} style.
        
        <match_events>
            {relevant_events_json}
        </match_events>
        """

        narration = self.model.generate_text(prompt)

        return GameNarrativeDTO(narration=narration)
