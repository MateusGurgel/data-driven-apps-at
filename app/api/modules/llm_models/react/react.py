from decouple import config
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import OpenAI

from api.modules.llm_models.llm_interface import LlmModel

from api.modules.llm_models.react.get_match_data_tool import get_match_data
from api.modules.llm_models.react.get_player_data_tool import get_player_data


class ReactAgent(LlmModel):

    def __init__(self):

        tools = [get_match_data, get_player_data]
        prompt = hub.pull("hwchase17/react")
        llm = OpenAI(openai_api_key=config("OPENAI_API_KEY"))
        agent = create_react_agent(llm, tools, prompt)
        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def generate_text(self, text: str) -> str:
        return self.agent_executor.invoke({"input": text})["output"]

    def generate_text_with_json_response(self, text: str) -> dict:
        raise NotImplementedError