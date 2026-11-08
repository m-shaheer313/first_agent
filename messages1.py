from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()


model = init_chat_model("openai:gpt-6-luna")
messages = [
    SystemMessage("You are a pirate. Answer in one short sentence."),
    HumanMessage("What is Python?"),
]


response = model.invoke(messages)
print(type(response))
print(response.text)

# ====================================== Memory ===============================================

messages.append(response)
messages.append(HumanMessage("Say that again in Urdu."))

response2 = model.invoke(messages)
print(response2.text)