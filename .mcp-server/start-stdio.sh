#!/bin/bash
# Portable MCP Server Startup Script (stdio transport for Claude Code)
# Automatically finds vault location and sets up Python environment

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT_DIR="$(dirname "$SCRIPT_DIR")"
VENV_DIR="$SCRIPT_DIR/.venv"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+" >&2
    exit 1
fi

# Create venv if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR" 2>&1 >/dev/null
fi

# Activate venv
source "$VENV_DIR/bin/activate"

# Install/upgrade dependencies silently
pip install -q --upgrade pip 2>&1 >/dev/null
pip install -q mcp pyyaml 2>&1 >/dev/null

# Start the MCP server (no output to stdout/stderr except server protocol)
export VAULT_PATH="$VAULT_DIR"
exec python3 "$SCRIPT_DIR/mcp_server_stdio.py"

# Note: exec replaces this process, so cleanup happens automatically when server exits
