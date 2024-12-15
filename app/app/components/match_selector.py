from statsbombpy import sb
import streamlit as st

def get_selected_match(key: str):
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

    return str(selected_match["match_id"].item())