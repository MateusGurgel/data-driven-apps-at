import streamlit as st

from api.get_event_summary import get_event_summary
from api.get_narration import get_narration
from api.get_player_profile import get_player_profile
from components.match_player_selector import match_player_selector
from components.match_selector import get_selected_match


def player_profile():
    st.header("⚽ Perfil do Jogador")
    player_id, match_id = match_player_selector("PlayerProfile")

    st.write("Resumo das jogadas dos jogadores:")
    with st.spinner("Resumindo os eventos da partida..."):
        summary = get_player_profile(player_id, match_id)
        st.write(summary)

def event_summary():
    st.header("📊 Sumarização de Eventos")

    selected_match = get_selected_match("EventSummary")

    st.write("Resumo dos eventos da partida:")
    with st.spinner("Resumindo os eventos da partida..."):
        summary = get_event_summary(selected_match)
        st.write(summary)

def custom_narration():
    st.header("🎙️ Narração Personalizada")

    selected_match = get_selected_match("MatchNarration")

    # Narration Style Selection
    narration_styles = ["Formal", "Humorist", "Technical"]
    selected_narration_style = st.selectbox("Selecione o estilo da narração", narration_styles)

    st.write("Resumo dos eventos da partida:")
    with st.spinner("Resumindo os eventos da partida..."):
        narration = get_narration(selected_match, selected_narration_style)
        st.write(narration)

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