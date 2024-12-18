from decouple import config
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool

from api.modules.llm_models.llm_interface import LlmModel
from langchain_google_genai import GoogleGenerativeAI

from api.modules.llm_models.react.get_match_data_tool import get_match_data
from api.modules.llm_models.react.get_player_data_tool import get_specific_player_data
from api.modules.llm_models.react.get_passes import get_passes


class ReactAgent(LlmModel):

    def __init__(self):

        tools = [get_match_data, get_specific_player_data, get_passes]
        prompt = hub.pull("hwchase17/react")
        llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.2, google_api_key=config("GEMINI_TOKEN"))
        agent = create_react_agent(llm, tools, prompt)
        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def generate_text(self, text: str) -> str:
        return self.agent_executor.invoke({"input": text})["output"]

    def generate_text_with_json_response(self, text: str) -> dict:
        raise NotImplementedError