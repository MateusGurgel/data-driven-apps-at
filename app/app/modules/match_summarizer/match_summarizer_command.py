from fastapi import HTTPException
from statsbombpy import sb

from modules.llm_models.llm_interface import LlmModel
from modules.match_summarizer.match_summarizer_dto import CreateMatchSummaryDTO, MatchSummaryDTO


class MatchSummaryCommand:
    def __init__(self, model: LlmModel):
        self.model = model

    def execute(self, create_match_summary: CreateMatchSummaryDTO) -> MatchSummaryDTO:
        """
        This method summarizes the events of a match using the Gemini model.
        """

        try:
            events = sb.events(match_id=create_match_summary.match_id)
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

        relevant_events_json = relevant_events.to_json(orient="records")

        prompt = f"""
        You are a professional football summarizer. 
        Your task is to summarize the events of a match in a concise and informative manner. 
        Please provide a comprehensive summary of the match, including key statistics, highlights, and insights.
        
        1. The Response should be in Portuguese.
        2. The Response should be in a clear and concise manner, avoiding jargon and technical terms.
        3. Be sure that even if the reader does not understand about soccer, they can understand the main points of the match.
        
        <match_events>
        {relevant_events_json}
        </match_events>
        """

        summary = self.model.generate_text(prompt)

        return MatchSummaryDTO(summary=summary)
