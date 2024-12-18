# Análise de Partidas de Futebol com FastAPI e Streamlit

## Descrição do Projeto
Este projeto tem como objetivo explorar o mundo do futebol utilizando tecnologias modernas para análise de dados, APIs e interfaces interativas. Ele consiste em criar uma aplicação data-driven focada em uma única partida de futebol, oferecendo perfis detalhados de jogadores, sumarização de eventos e narrativas personalizadas.

O projeto é desenvolvido em duas abordagens:
1. **FastAPI + LLM**: Uma API para geração de perfis de jogadores, sumarização e criação de narrativas.
2. **Streamlit + LangChain**: Uma interface interativa para explorar os dados da partida.

## Funcionalidades Principais
- **Perfil de Jogador**: Estatísticas detalhadas e análises sobre os jogadores da partida.
- **Sumarização de Eventos**: Transformação dos eventos em uma narrativa descritiva.
- **Narração Personalizada**: Geração de textos narrativos de acordo com estilos escolhidos pelos usuários.

## Como rodar o projeto

Criação do venv:

```bash
python -m venv venv
```

Ativação do venv:

```bash
source venv/bin/activate
```

Instalação das dependências:

```bash
pip install -r requirements.txt
```

Executação da api:

```bash
cd apps/services
uvicorn main:app --reload
```

Executação da interface:

```bash
cd apps/app
streamlit run app/main.py
```