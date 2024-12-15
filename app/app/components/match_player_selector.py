import streamlit as st
from statsbombpy import sb

def match_player_selector(key: str) -> tuple:
    competitions = sb.competitions()

    # Competition Selection
    competition_options = competitions["competition_name"].tolist()
    selected_competition_name = st.selectbox("Selecione a competição", competition_options, key=f"{key}:competition")
    selected_competition = competitions[competitions["competition_name"] == selected_competition_name].iloc[0]

    # Match Selection
    matches = sb.matches(competition_id=selected_competition["competition_id"], season_id=selected_competition["season_id"])
    match_options = matches["match_date"].tolist()
    selected_match_name = st.selectbox("Selecione a data da partida", match_options, key=f"{key}:match")
    selected_match = matches[matches["match_date"] == selected_match_name].iloc[0]

    # Get events for the selected match
    events = sb.events(match_id=selected_match["match_id"].item())
    events = sb.events(match_id=selected_match["match_id"])
    events = events.dropna(subset=['player_id'])

    # Player Selection
    player_options = events["player"].tolist()
    selected_player_name = st.selectbox("Selecione o jogador", player_options, key=f"{key}:player")
    selected_player = events[events["player"] == selected_player_name].iloc[0]

    return str(selected_player["player_id"].item()), str(selected_player["match_id"].item())