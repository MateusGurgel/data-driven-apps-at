import requests
from decouple import config
import streamlit as st


API_LINK = config("API_HOST")

st.cache_resource(ttl=3600)
def get_event_summary(match_id: str) -> str:

    if not isinstance(match_id, str):
        raise ValueError("match_id must be a string")

    url = API_LINK + "/summarize/"

    payload = {
        "match_id": match_id
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("Failed to get event summary")

    response_json = response.json()
    summary = response_json["summary"]

    return summary