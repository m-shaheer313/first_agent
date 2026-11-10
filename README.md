<div align="center">

# 🚀 Learn LangChain Agents
### *The Hands-On Engineering Playground for Autonomous AI Agents, Tools, Memory & Streaming*

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1.4+-1C3C3C?style=flat&logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![Package Manager](https://img.shields.io/badge/Package%20Manager-uv-DE5FE9?style=flat)](https://github.com/astral-sh/uv)
[![Architecture](https://img.shields.io/badge/Architecture-Agentic%20Workflows-00C49F?style=flat)](https://github.com/m-shaheer313/learn-langchain-agents)

<p align="center">
  A code-first, zero-fluff repository for mastering production-ready agentic patterns with <b>LangChain 1.4+</b>.<br>
  Step through practical implementations covering custom tool definitions, intelligent docstring routing, multi-turn state persistence, structured Pydantic extractions, real-time token streaming, and multi-tenant runtime context injection.
</p>

</div>

---

## 🌟 Key Capabilities at a Glance

| Capability | Description | Core Script |
| :--- | :--- | :--- |
| **Autonomous Tool Calling** | Dynamic function calling with typed parameters & LLM docstring schemas | [`agent1.py`](agent1.py), [`tools1.py`](tools1.py) |
| **Docstring-Driven Routing** | Natural language routing between domain-specific tools | [`tools2.py`](tools2.py) |
| **Multi-Turn Memory** | Stateful conversation retention via `InMemorySaver` checkpointer & `thread_id` | [`memory1.py`](memory1.py), [`messages1.py`](messages1.py) |
| **Structured Output Extraction** | Strict entity extraction directly into Pydantic models with validation | [`structured1.py`](structured1.py), [`questions1.py`](questions1.py) |
| **Real-Time Streaming** | Live token generation (`messages`), state values, and node updates | [`stream1.py`](stream1.py) |
| **Runtime Context Injection** | Server-side `ToolRuntime` context injection for secure multi-tenant scoping | [`context1.py`](context1.py) |

---

## Project Structure

```text
learn-langchain-agents/
├── .env.example       # Template for environment variables
├── .gitignore         # Ignores .venv, .env, __pycache__, etc.
├── .python-version    # Python 3.12 specification
├── pyproject.toml     # Project metadata and dependencies
├── README.md          # Project documentation
├── uv.lock            # Lockfile for reproducible dependencies
│
├── agent1.py          # Weather agent with tool calling and message inspection
├── messages1.py       # Chat model invocation, message schemas, and multi-turn memory
├── tools1.py          # @tool decorator, multi-tool binding, and schema inspection
├── tools2.py          # Docstring-based tool routing (pricing & stock inventory)
├── stream1.py         # Agent streaming modes (values, updates, and messages)
├── memory1.py         # Checkpointer memory with InMemorySaver and thread_id
├── structured1.py     # Structured response extraction using Pydantic models
├── questions1.py      # Pydantic validation, schema inspection & structured vs plain agent comparison
└── context1.py        # Runtime context injection into tools with ToolRuntime and context_schema
```

---

## Modules & Examples

### 1. [`agent1.py`](agent1.py) — Basic Tool-Calling Agent
- Creates an agent via `create_agent`.
- Binds a custom weather function tool (`get_weather`).
- Inspects message chains with `m.pretty_print()` and extracts AI tool call payloads via `ai_msg.tool_calls`.

### 2. [`messages1.py`](messages1.py) — Chat Models & Conversational Memory
- Uses `init_chat_model` for model initialization.
- Works with structured message types: `SystemMessage` and `HumanMessage`.
- Demonstrates stateful multi-turn memory by appending model responses and subsequent user inputs into the conversation history.

### 3. [`tools1.py`](tools1.py) — Tool Definition & Schema Inspection
- Uses the `@tool` decorator to turn Python functions into LangChain tools (`add`, `get_weather`).
- Binds multiple tools to a single agent.
- Inspects generated tool metadata including `add.name`, `add.description`, and `add.args`.

### 4. [`tools2.py`](tools2.py) — Tool Routing via Docstrings
- Implements e-commerce inventory tools: `tool_a` (product pricing) and `tool_b` (stock quantity).
- Demonstrates how LLMs use natural language docstrings to intelligently route queries to the correct tool.

### 5. [`stream1.py`](stream1.py) — Agent Streaming Modes
Demonstrates the three core streaming modes available in `agent.stream`:
- **`stream_mode="values"`**: Streams full conversation state step-by-step.
- **`stream_mode="updates"`**: Streams state updates produced by individual graph nodes.
- **`stream_mode="messages"`**: Streams token-by-token text output in real-time (`token.text`).

### 6. [`memory1.py`](memory1.py) — Checkpointer Memory with Threads
- Uses `InMemorySaver` checkpointer with `create_agent`.
- Manages independent conversation sessions using `configurable: {"thread_id": "..."}`.
- Demonstrates state persistence across turns within a thread and isolation across distinct threads.

### 7. [`structured1.py`](structured1.py) — Structured Output Extraction
- Defines strongly-typed schemas using Pydantic (`ContactInfo`).
- Configures `create_agent` with `response_format = ContactInfo`.
- Extracts structured entity data (`name`, `email`, `phone`) from unstructured natural language text accessible via `result["structured_response"]`.

### 8. [`questions1.py`](questions1.py) — Validation & Agent Response Comparison
- Demonstrates Pydantic field constraints (`ge=0, le=100`, optional fields) and `ValidationError` handling.
- Inspects generated JSON schema using `model_json_schema()`.
- Contrasts plain agents (returning unstructured text in `messages`) with structured agents (returning typed Pydantic instances in `structured_response`).

### 9. [`context1.py`](context1.py) — Runtime Context Injection
- Demonstrates injecting server-side runtime context (`ToolRuntime[Context]`) into tools.
- Defines a dataclass `Context(user_id=...)` configured via `context_schema = Context`.
- Context parameters are securely provided at runtime and hidden from the LLM tool parameter schema (`get_balance.args`).
- Enables secure multi-tenant scoping and per-user state lookups (`agent.invoke(..., context=Context(...))`).

---

## Prerequisites

- **Python**: 3.12 or higher
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (recommended) or standard `pip` / `venv`
- **OpenAI API Key**: Required for model calls

---

## Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/m-shaheer313/learn-langchain-agents.git
   cd learn-langchain-agents
   ```

2. **Install dependencies**:

   **Using `uv` (recommended):**
   ```bash
   uv sync
   ```

   **Using `pip` & `venv`:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows PowerShell: .venv\Scripts\Activate.ps1
   pip install -e .
   ```

3. **Configure Environment Variables**:
   Copy the sample environment file:
   ```bash
   cp .env.example .env  # On Windows PowerShell: Copy-Item .env.example .env
   ```
   Add your OpenAI API key in `.env`:
   ```env
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

---

## Running the Examples

Run any script using Python or `uv run`:

```bash
# Basic agent with tool call inspection
python agent1.py

# Chat model invocation and memory demonstration
python messages1.py

# @tool decorator and schema inspection
python tools1.py

# Dynamic tool routing demonstration
python tools2.py

# Streaming tokens, node updates, and state values
python stream1.py

# Thread-based memory persistence with checkpointer
python memory1.py

# Structured response extraction with Pydantic
python structured1.py

# Pydantic validation & agent comparison
python questions1.py

# Runtime context injection into tools
python context1.py
```

> [!NOTE]
> **Model Configuration:** The code examples use `gpt-6-luna` as a placeholder model identifier. For live production use with OpenAI's API, replace this with an active model such as `gpt-4o` or `gpt-4o-mini` in the respective script.
