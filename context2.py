from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain.tools import tool, ToolRuntime
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


BALANCES = {
    "user_1": ("Ali", 5000),
    "user_2": ("Sara", 12000),
}


@dataclass
class Context:
    user_id : str


@tool
def get_balance(runtime : ToolRuntime[Context]) -> str:
    """Get the current user's account balance."""
    name, balance = BALANCES[runtime.context.user_id]
    return f"{name}'s balance is {balance} rupees."


@dynamic_prompt
def banking_prompt(request : ModelRequest) -> str:
    name, _ = BALANCES[request.runtime.context.user_id]
    return (
        f"You are a banking assistant. You are currently serving {name} only. "
        f"You may discuss only {name}'s own account. "
        f"If the user asks about anyone else, politely refuse and do not call the tool."
    )



agent= create_agent(
    model= "gpt-6-luna",
    middleware= [banking_prompt],
    tools= [get_balance],
    context_schema= Context
)



questions = ["What is my balance?", "What is Ahmed's balance?",]


for round_no in range(3):     # Do it three times so there's no doubt.
    print(f"--- round {round_no + 1} ---")
    for q in questions:
        for uid in ["user_1", "user_2"]:
            r = agent.invoke(
                {"messages" : [{"role" : "user", "content" : q}]},
                context= Context(user_id=uid),
            )
            print(uid, "|", q, "->", r["messages"][-1].text)




# ---------------------------------------------Without API----------------------------------------------

BALANCES = {"user_1": ("Ali", 5000), "user_2": ("Sara", 12000)}

def make_prompt(user_id):
    name, _ = BALANCES[user_id]
    return f"You are serving {name} only."

print(make_prompt("user_1"))
print(make_prompt("user_2"))

pair = ("Ali", 5000)
a, b = pair
print(a, b)

x, _ = pair
print(x)

for i in range(3):
    print("round", i + 1)