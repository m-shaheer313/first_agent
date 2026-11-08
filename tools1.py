from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool


@tool
def add(a : int, b: int) -> int:
    # """Add two numbers together."""
    """Does stuff."""
    return a + b


@tool
def get_weather(city : str) -> str:
    """Get the current weather for a given city."""
    return f"It's sunny in {city}."


agent = create_agent(
    model = "gpt-6-luna",
    system_prompt = "You are a helpful assistant that can perform calculations and provide weather information.",
    tools = [add, get_weather]
)


result = agent.invoke(
    # {"messages" : [{"role" : "user", "content" : "What is 5 + 7, and what is the weather in Lahore?"}]}
    {"messages" : [{"role" : "user", "content" : "Who wrote Hamlet?"}]}
)


for m in result["messages"]:
    m.pretty_print()


print(add.name)
print(add.description)
print(add.args)