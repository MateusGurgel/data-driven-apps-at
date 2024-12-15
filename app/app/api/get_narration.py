from typing import Literal

import requests
from decouple import config
import streamlit as st


API_LINK = config("API_HOST")

st.cache_data()
def get_narration(match_id: str, style: Literal["Formal", "Humorist", "Technical"]) -> str:

    if not isinstance(match_id, str):
        raise ValueError("match_id must be a string")

    url = API_LINK + "/game_narrator/"

    payload = {
        "match_id": match_id,
        "narrative_style": style
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("Failed to get event narration")

    response_json = response.json()
    summary = response_json["narration"]

    return summary