import requests
from decouple import config
import streamlit as st


API_LINK = config("API_HOST")

st.cache_data()
def get_player_profile(player_id: str, match_id: str) -> tuple:

    if not isinstance(player_id, str):
        raise ValueError("player_id must be a string")

    if not isinstance(match_id, str):
        raise ValueError("match_id must be a string")

    url = API_LINK + "/profile/"

    payload = {
        "match_id": match_id,
        "player_id": player_id
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("Failed to get event summary")

    response_json = response.json()
    summary = response_json["summary"]
    events = response_json["events"]

    return summary, events