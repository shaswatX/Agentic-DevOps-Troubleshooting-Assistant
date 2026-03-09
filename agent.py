from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from tools.log_analyzer import analyze_log
from tools.search_tool import search_error
from tools.shell_tool import run_shell
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

agent = initialize_agent(
    tools=[analyze_log, search_error, run_shell],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)


def troubleshoot(log):
    prompt = f"""
You are an AI DevOps assistant.

Tasks:
1. Analyze server errors
2. Identify root cause
3. Suggest fix
4. Run shell commands if required

Server log:
{log}
"""

    response = agent.invoke({"input": prompt})
    return response["output"]