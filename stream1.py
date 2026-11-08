from langchain.agents import create_agent
from langchain.tools import tool

from dotenv import load_dotenv
load_dotenv()


@tool
def get_weather(city : str) -> str:
    """Get the current weather for a city."""
    return f"It's sunny in {city}."



agent = create_agent(
    model = "gpt-6-luna",
    tools = [get_weather],
    system_prompt = "You are a helpful assistant that can provide weather information for cities."
)

question = {
    "messages" : [{"role" : "user",
    "content" : "What's the weather like in New York City?"}]
}



print("--- values ---")
for step in agent.stream(question, stream_mode = "values"):
    step["messages"][-1].pretty_print()


print("\n--- updates ---")
for chunk in agent.stream(question, stream_mode = "updates"):
    for node, data in chunk.items():
        print(f"Node: {node}")


print("\n--- messages ---")
for token, metadata in agent.stream(question, stream_mode = "messages"):
    # if metadata["langgraph_node"] == "model":
        print(token.text, end = "", flush = True)


print()