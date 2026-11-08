from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


def get_weather(city : str) -> str:
    """Get weather for a given city"""
    return f"It's always sunny in {city} :)"


agent = create_agent(
        model = "gpt-6-luna",
        system_prompt = "You are a helpful assistant that provides weather information.",
        tools = [get_weather]
    )


result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather like in London?"}]}
)

print(result["messages"][-1].content)