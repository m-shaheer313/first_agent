# First Agent - LangChain Weather Assistant

A lightweight AI agent built with **LangChain 1.4+** that demonstrates tool calling and conversational agent workflows using Python.

## Overview

This project implements an autonomous agent equipped with a weather retrieval tool. The agent:
- Utilizes LangChain's `create_agent` workflow.
- Integrates a Python tool function (`get_weather`) with typed inputs and docstrings for LLM tool binding.
- Manages credentials securely using `python-dotenv`.
- Operates on a standard messages-based state (`messages` input and output schema).

## Project Structure

```
first_agent/
├── .env.example       # Template for environment variables
├── .gitignore          # Ignores .venv, .env, __pycache__, etc.
├── .python-version    # Python 3.12 specification
├── agent1.py          # Main entrypoint implementing the weather agent
├── pyproject.toml     # Project metadata and dependencies
├── README.md          # Project documentation
└── uv.lock            # Lockfile for reproducible dependencies
```

## Prerequisites

- **Python**: 3.12 or higher
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (recommended) or standard `pip` / `venv`
- **OpenAI API Key**: Required for OpenAI model execution

## Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd first_agent
   ```

2. **Set up the virtual environment and install dependencies**:
   Using `uv`:
   ```bash
   uv sync
   ```
   Or using standard `pip`:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

3. **Configure Environment Variables**:
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env  # On Windows PowerShell: Copy-Item .env.example .env
   ```
   Add your OpenAI API key in `.env`:
   ```env
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

## Usage

Run the agent script:
```bash
python agent1.py
```
Or with `uv`:
```bash
uv run agent1.py
```

> **Note on Model Configuration:**
> `agent1.py` is configured with `model="gpt-6-luna"`. For standard OpenAI API usage, update this to an available model such as `gpt-4o` or `gpt-4o-mini` if needed.
