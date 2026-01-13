"""Entry point for Zeabur deployment."""

import os
import sys

# Add src directory to Python path for module imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from creative_agent.server import mcp

# Get port from environment (Zeabur sets this)
PORT = int(os.getenv("PORT", "8080"))

if __name__ == "__main__":
    # Run in HTTP mode (Streamable HTTP) for MCP clients
    # This exposes the server at /mcp endpoint
    mcp.run(transport="http", port=PORT, host="0.0.0.0")
