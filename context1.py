from langchain.agents import create_agent
from langchain.tools import tool,ToolRuntime

from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()


BALANCES = {
    "user_1": ("Ali", 5000), "user_2": ("Ahmed", 12000)
}


@dataclass
class Context:
    user_id : str


@tool
def get_balance(runtime: ToolRuntime[Context]) -> str:
    """Get the current user's account balance."""
    name, balance = BALANCES[runtime.context.user_id]
    return f"{name}'s account balance is {balance} rupees."


agent = create_agent(
    model= "gpt-6-luna",
    system_prompt= "You are a banking assistant. You can help users check their account balance.",
    tools= [get_balance],
    context_schema= Context,
)


question = {"messages" : [{"role" : "user", "content" : "What is my balance?"}]}

for uid in ["user_1", "user_2"]:
    result = agent.invoke(question, context= Context(user_id= uid))
    print(uid, "->", result["messages"][-1].text)


print(get_balance.args)  # This will print the argument schema for the get_balance tool