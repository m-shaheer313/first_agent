from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool


@tool
def tool_a(x: str) -> str:
    """Get the price of a product."""
    # """Does stuff."""
    return f"Price of {x} is 100 rupees."

@tool
def tool_b(x: str) -> str:
    """Get the stock quantity of a product."""
    # """Does stuff."""
    return f"Stock of {x} is 5 units."


agent = create_agent(
    model = "gpt-6-luna",
    system_prompt = "You are a helpful assistant that can perform calculations and provide weather information.",
    tools = [tool_a, tool_b]
)


result = agent.invoke(
    # {"messages" : [{"role" : "user", "content" : "What is 5 + 7, and what is the weather in Lahore?"}]}
    {"messages" : [{"role" : "user", "content" : "How many laptops are in stock?"}]}
)


for m in result["messages"]:
    m.pretty_print()