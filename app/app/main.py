import pandas as pd
import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler
from matplotlib import pyplot as plt

from modules.react_agent import react_agent_command
from modules.react_agent.react_agent_dto import GetAgentResponseDTO
from modules.game_narrator.game_narrator_dto import CreateGameNarrativeDTO
from modules.game_narrator import game_narrator_command
from modules.match_summarizer import match_summarizer_command
from modules.match_summarizer.match_summarizer_dto import CreateMatchSummaryDTO
from modules.player_profiler import player_profiler_command
from modules.player_profiler.player_profiler_dto import CreatePlayerProfileDTO
from components.match_player_selector import match_player_selector
from components.match_selector import get_selected_match


def player_profile():
    st.header("⚽ Perfil do Jogador")
    player_id, match_id = match_player_selector("PlayerProfile")

    st.write("Resumo das jogadas dos jogadores:")
    with st.spinner("Resumindo os eventos da partida..."):
        result = player_profiler_command.execute(CreatePlayerProfileDTO(player_id=player_id, match_id=match_id))
        events_df = pd.DataFrame(result.events)

        st.write(result.summary)
        st.write("📊 Dados sobre os Eventos:")

        # Calculate key statistics
        total_events = len(events_df)
        successful_shots = len(events_df[events_df['shot_outcome'] == 'Goal'])
        success_rate = (successful_shots / total_events * 100) if total_events > 0 else 0

        # Display metrics
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.metric("Total de Ações", total_events)

        with col2:
            st.metric("Gols Marcados", successful_shots)

        with col3:
            st.metric("Taxa de Sucesso", f"{success_rate:.1f}%")

        # Criar gráfico de barras com pandas
        if not events_df.empty:
            st.subheader("📈 Distribuição dos Tipos de Chute")

            # Criar contagem de eventos
            shot_counts = events_df['shot_outcome'].value_counts()

            # Criar gráfico de barras
            fig = shot_counts.plot(
                kind='bar',
                figsize=(10, 6),
                color=['#2ecc71', '#3498db', '#e74c3c', '#f1c40f'],
                title='Distribuição dos Tipos de Chute'
            ).get_figure()

            # Customizar o gráfico
            plt.xlabel('Resultado do Chute')
            plt.ylabel('Quantidade')
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Mostrar o gráfico no Streamlit
            st.pyplot(fig)
            plt.close()

        st.write("📊 Eventos Importantes:")
        st.write(result.events)


def event_summary():
    st.header("📊 Sumarização de Eventos")

    selected_match = get_selected_match("EventSummary")

    st.write("Resumo dos eventos da partida:")
    with st.spinner("Resumindo os eventos da partida..."):
        result = match_summarizer_command.execute(CreateMatchSummaryDTO(match_id=selected_match))
        st.write(result.summary)

def event_agent():
    st.header("🤖 Agente de Eventos")
    selected_match = get_selected_match("AgentEvent")
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            result = react_agent_command.execute(GetAgentResponseDTO(match_id=selected_match, question=prompt))
            st.write(result.summary)


def custom_narration():
    st.header("🎙️ Narração Personalizada")

    selected_match = get_selected_match("MatchNarration")

    # Narration Style Selection
    narration_styles = ["Formal", "Humorist", "Technical"]
    selected_narration_style = st.selectbox("Selecione o estilo da narração", narration_styles)

    st.write("Resumo dos eventos da partida:")
    with st.spinner("Resumindo os eventos da partida..."):
        result = game_narrator_command.execute(CreateGameNarrativeDTO(match_id=selected_match, narrative_style=selected_narration_style))
        st.write(result.narration)

def main():
    st.title("⚽ Análise de Partidas de Futebol")

    tabs = st.tabs(["Perfil de Jogador", "Sumarização de Eventos", "Narração Personalizada", "Agente de Eventos"])

    with tabs[0]:
        player_profile()

    with tabs[1]:
        event_summary()

    with tabs[2]:
        custom_narration()

    with tabs[3]:
        event_agent()

if __name__ == '__main__':
    main()