#cli
from agents.researcher_agent import get_research_agent

if __name__ == "__main__":
    agent = get_research_agent()
    agent.run("Research the impact of LLMs on education")
