from langchain.agents import create_agent
from pydantic import BaseModel, Field


from dotenv import load_dotenv
load_dotenv()


class ContactInfo(BaseModel):
    """Contact information for a person."""
    name : str = Field(description = "The name of the person.")
    email : str = Field(description = "The email address of the person.")
    phone : str = Field(description = "The phone number of the person.")



agent = create_agent(
    model = "gpt-6-luna",
    response_format = ContactInfo,
)


text = ("""We talked with John Doe. He works over at Example. His number is,
        let's see, five five five, one two three, four five six seven.
        Did you get that? And his email was john at example.com. 
        He wanted to order 50 boxes of Captain Crunch.""")


result = agent.invoke(
    {"messages" : [{"role" : "user", "content" : f"Extract the contact information: {text}"}]}
)


info = result["structured_response"]
print(type(info))
print(info)
print(info.name, info.email, info.phone)