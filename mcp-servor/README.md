# MCP Calculator Server

A simple MCP (Model Context Protocol) server implemented in Python, providing basic arithmetic tools for any MCP client.

## Features

- **Built with Python & FastMCP**: Easy to maintain and extend.
- **Calculator Tools**: Standard arithmetic operations (`add`, `subtract`, `multiply`, `divide`).
- **Stdio Transport**: Efficient and light-weight communication.

## Quick Start

### 1. Installation

Ensure you have Python 3.10+ installed. It is recommended to use a virtual environment.

```bash
# Recommended: Create a virtual environment
python -m venv .venv
# Activate (Windows)
.\.venv\Scripts\activate
# Activate (macOS/Linux)
# source .venv/bin/activate

# Install the MCP SDK
pip install mcp[cli]
```

### 2. Running Locally

You can start the server manually for debugging (it runs via standard input/output):

```bash
python server.py
```

*Note: Since this is an stdio server, it will wait for JSON-RPC messages from a client.*

## Testing with MCP Inspector

MCP Inspector is a valuable tool for testing servers independently of an LLM.

```bash
npx @modelcontextprotocol/inspector python server.py
```

This will launch a web interface at `http://localhost:5173` (or similar) where you can list and trigger your calculator tools.

## Integration with Antigravity Desktop

To use this server with your Antigravity Desktop application, update your `antigravity_config.json` file as follows:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["c:/Users/Samuel/Documents/AI-automation/agentic-ai-bootcamp/mcp-servor/server.py"]
    }
  }
}
```

*Be sure to use the absolute path to `server.py`.*
