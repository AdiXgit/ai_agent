from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOllama
from tools.search_tool import search_google
from tools.extract_tool import extract_text
from tools.summarise_tool import summarise_article


llm = ChatOllama(model = "mistral")
tools = [
    Tool(name="SearchTool", func=search_google, description="Google search tool for finding links"),
    Tool(name="ExtractTool", func=extract_text, description="Extracts readable text from a webpage"),
    Tool(name="SummarizeTool", func=summarise_article, description="Summarizes a given article text"),
]

def get_research_agent():
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
