"""Entry point for Zeabur deployment."""

import os
from creative_agent.server import mcp

# Get port from environment (Zeabur sets this)
PORT = int(os.getenv("PORT", "8080"))

if __name__ == "__main__":
    # Run in SSE mode for HTTP deployment
    mcp.run(transport="sse", port=PORT, host="0.0.0.0")
