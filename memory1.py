from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from dotenv import load_dotenv
load_dotenv()



agent = create_agent(
    model = "gpt-6-luna",
    system_prompt = "You are a helpful assistant.",
    checkpointer = InMemorySaver()
)


chat1 = {"configurable" : {"thread_id" : "chat-1"}}
chat2 = {"configurable" : {"thread_id" : "chat-2"}}


r1 = agent.invoke({
    "messages" : [{"role" : "user", "content" : "My name is Ali:)"}]}, chat1)
print(r1["messages"][-1].text)


r2 = agent.invoke({
    "messages" : [{"role" : "user", "content" : "What is my name?"}]}, chat1)
print(r2["messages"][-1].text)

r3 = agent.invoke(
    {"messages" : [{"role" : "user", "content" : "What is my name?"}]}, chat2)
print(r3["messages"][-1].text)

print(len(r1["messages"]), len(r2["messages"]), len(r3["messages"]))
