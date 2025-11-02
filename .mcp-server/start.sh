#!/bin/bash
# Portable MCP Server Startup Script
# Automatically finds vault location and sets up Python environment

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT_DIR="$(dirname "$SCRIPT_DIR")"
VENV_DIR="$SCRIPT_DIR/.venv"
MCP_PORT="${MCP_PORT:-3000}"

echo "=========================================="
echo "🚀 Redstack Vault MCP Server"
echo "=========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Create venv if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Virtual environment created"
fi

# Activate venv
echo ""
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"
echo "✓ Virtual environment activated"

# Install/upgrade dependencies
echo ""
echo "Checking dependencies..."
pip install -q --upgrade pip
pip install -q mcp starlette uvicorn pyyaml
echo "✓ Dependencies installed"

echo ""
echo "=========================================="
echo "Starting MCP Server"
echo "=========================================="
echo ""
echo "Vault Path: $VAULT_DIR"
echo "MCP Server: http://localhost:$MCP_PORT"
echo "SSE Endpoint: http://localhost:$MCP_PORT/sse"
echo ""
echo "📚 9 MCP tools available"
echo "🔗 Connect with AnythingLLM, Claude Desktop, etc."
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Start the MCP server (no need to set VAULT_PATH, script auto-detects)
export MCP_PORT
python3 "$SCRIPT_DIR/mcp_server_sse.py"

# Deactivate venv on exit
trap "deactivate" EXIT
