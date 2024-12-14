from statsbombpy import sb
import streamlit as st

def player_profile():
    st.header("⚽ Perfil do Jogador")
    # Área para implementar análise detalhada de jogadores
    pass

def event_summary():
    st.header("📊 Sumarização de Eventos")

    competitions = sb.competitions()

    # Competition Selection
    competition_options = competitions["competition_name"].tolist()
    selected_competition_name = st.selectbox("Selecione a competição", competition_options)
    selected_competition = competitions[competitions["competition_name"] == selected_competition_name].iloc[0]

    # Match Selection
    matches = sb.matches(competition_id=selected_competition["competition_id"], season_id=selected_competition["season_id"])
    match_options = matches["match_date"].tolist()
    selected_match_name = st.selectbox("Selecione a data da partida", match_options)
    selected_match = matches[matches["match_date"] == selected_match_name].iloc[0]

    events = sb.events(match_id=selected_match["match_id"])

    events

def custom_narration():
    st.header("🎙️ Narração Personalizada")
    # Área para implementar geração de narrações personalizadas
    pass

def main():
    st.title("⚽ Análise de Partidas de Futebol")

    tabs = st.tabs(["Perfil de Jogador", "Sumarização de Eventos", "Narração Personalizada"])

    with tabs[0]:
        player_profile()

    with tabs[1]:
        event_summary()

    with tabs[2]:
        custom_narration()

if __name__ == '__main__':
    main()