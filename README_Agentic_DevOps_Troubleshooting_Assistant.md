# Agentic DevOps Troubleshooting Assistant

An AI-powered DevOps troubleshooting system that analyzes server error
logs, performs reasoning using an LLM agent, and suggests possible fixes
automatically.

This project demonstrates how Agentic AI systems can automate debugging
workflows in DevOps environments by combining LLM reasoning, tool
execution, and system diagnostics.

------------------------------------------------------------------------

## Project Overview

Modern applications generate large volumes of logs, and diagnosing
production errors can be time‑consuming.

The Agentic DevOps Troubleshooting Assistant addresses this problem by:

-   Accepting server error logs
-   Using an LLM agent for reasoning
-   Calling diagnostic tools
-   Suggesting root causes and solutions

The system acts as a DevOps debugging assistant capable of analyzing
infrastructure errors and recommending fixes.

------------------------------------------------------------------------

## Architecture

Server Error Log\
↓\
FastAPI API Endpoint\
↓\
Agent Reasoning (LangChain Agent)\
↓\
Groq LLM\
↓\
Tool Execution

-   Log Analyzer\
-   Web Search\
-   Shell Command Executor

↓\
Root Cause + Fix Recommendation

------------------------------------------------------------------------

## Example Workflow

### Input Log

``` json
{
"log": "ModuleNotFoundError: No module named 'numpy'"
}
```

### Output

Root Cause:\
The numpy package is not installed in the Python environment.

Fix:\
Install numpy using pip.

Command:\
pip install numpy

------------------------------------------------------------------------

## Features

-   AI-powered log analysis
-   Agent-based reasoning
-   Tool calling architecture
-   Shell command diagnostics
-   Web search for troubleshooting information
-   FastAPI REST interface

------------------------------------------------------------------------

## Tech Stack

  Component              Technology
  ---------------------- -------------------------------------------
  Backend API            FastAPI
  Agent Framework        LangChain
  LLM Provider           Groq
  Programming Language   Python
  Tools                  Log Analyzer, Web Search, Shell Execution

------------------------------------------------------------------------

## Project Structure

    ai-devops-agent
    │
    ├── main.py
    ├── agent.py
    │
    ├── tools
    │   ├── log_analyzer.py
    │   ├── search_tool.py
    │   └── shell_tool.py
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Installation

Clone the repository:

``` bash
git clone https://github.com/yourusername/agentic-devops-troubleshooting-assistant.git
```

Navigate to the project directory:

``` bash
cd agentic-devops-troubleshooting-assistant
```

Create a virtual environment:

``` bash
python -m venv .venv
```

Activate the environment (Windows):

``` bash
.venv\Scripts\activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Environment Setup

Create a `.env` file and add your Groq API key:

    GROQ_API_KEY=your_api_key_here

------------------------------------------------------------------------

## Running the Application

Start the FastAPI server:

``` bash
uvicorn main:app --reload
```

Open API documentation:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Example Test Request

POST /analyze

``` json
{
"log": "OSError: [Errno 98] Address already in use"
}
```

Expected response:

Root Cause: Port already in use\
Fix: Stop the process using the port

------------------------------------------------------------------------

## Future Improvements

-   Docker container log analysis
-   Kubernetes log monitoring
-   Real-time log ingestion
-   Cloud deployment (AWS / GCP)
-   Automated remediation workflows

------------------------------------------------------------------------

## License

MIT License
