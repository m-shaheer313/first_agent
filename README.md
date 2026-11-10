# First Agent - LangChain Agent & Tools Playground

A practical hands-on guide and exploration of building autonomous AI agents, custom tools, conversation memory, and real-time streaming with **LangChain 1.4+** in Python.

---

## Overview

This repository demonstrates modern agentic workflows powered by LangChain. It covers foundational agent patterns from simple tool-calling agents to multi-turn conversation memory, dynamic tool routing based on docstrings, and streaming tokens/state updates.

---

## Project Structure

```text
first_agent/
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
└── structured1.py     # Structured response extraction using Pydantic models
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

---

## Prerequisites

- **Python**: 3.12 or higher
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (recommended) or standard `pip` / `venv`
- **OpenAI API Key**: Required for model calls

---

## Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/m-shaheer313/first_agent.git
   cd first_agent
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
```

> [!NOTE]
> **Model Configuration:** The code examples use `gpt-6-luna` as a placeholder model identifier. For live production use with OpenAI's API, replace this with an active model such as `gpt-4o` or `gpt-4o-mini` in the respective script.
