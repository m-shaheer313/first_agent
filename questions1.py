from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field, ValidationError
from langchain.agents import create_agent

class Student(BaseModel):
    name: str
    marks: int = Field(ge=0, le=100, description="Marks out of 100")
    city: str | None = Field(default=None, description="City, if mentioned")

# ---------- Sawal 1: Field ----------
s = Student(name="Ali", marks=85)
print(s)                                    # name='Ali' marks=85 city=None

try:
    Student(name="Sara", marks=150)         # 100 se zyada!
except ValidationError as e:
    print("Error:", e.errors()[0]["msg"])   # Pydantic ne rok diya

print(Student.model_json_schema())          # ye wo cheez hai jis mein description jati hai

# ---------- Sawal 2 aur 3: response_format aur structured_response ----------
q = {"messages": [{"role": "user", "content": "Ali from Lahore got 85 marks."}]}

agent_plain = create_agent(model="openai:gpt-5")                          # apni model line
agent_form = create_agent(model="openai:gpt-5", response_format=Student)

r1 = agent_plain.invoke(q)
print(r1.keys())                            # sirf 'messages'
print(r1["messages"][-1].text)              # aam text jumla

r2 = agent_form.invoke(q)
print(r2.keys())                            # 'messages' aur 'structured_response'
print(r2["structured_response"])            # Student object
print(r2["structured_response"].marks + 5)  # number ki tarah kaam karta hai: 90