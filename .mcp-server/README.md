# Redstack Vault MCP Server

Model Context Protocol (MCP) server for the Redstack TTP Vault. Provides structured access to 2000+ procedures, 4000+ commands, and attack chains through a standardized interface.

## 🚀 Quick Start

```bash
# From anywhere, just run:
cd /path/to/redstack-vault/output/.mcp-server
./start.sh
```

The server will:
- Auto-detect the vault location (parent directory)
- Create a Python virtual environment
- Install dependencies automatically
- Start on http://localhost:3000

## 📋 Requirements

- Python 3.9 or higher
- Internet connection (first run only, for dependencies)

## 🔌 Integration

### AnythingLLM Desktop

1. Start the MCP server: `./start.sh`
2. Add to AnythingLLM config at:
   ```
   ~/Library/Application Support/anythingllm-desktop/storage/plugins/anythingllm_mcp_servers.json
   ```

   ```json
   {
     "mcpServers": {
       "redstack": {
         "url": "http://localhost:3000/sse",
         "disabled": false,
         "alwaysAllow": [],
         "type": "sse"
       }
     }
   }
   ```

3. Restart AnythingLLM
4. Tools will appear in Custom Skills

### Claude Desktop

Add to Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "redstack": {
      "command": "/path/to/output/.mcp-server/start.sh"
    }
  }
}
```

### Claude Code (CLI)

Claude Code uses stdio transport instead of SSE. Two setup options:

**Option 1: Auto-configuration (Recommended)**
```bash
# Just open Claude Code in the redstack-vault directory
# The .mcp.json file will auto-configure the server
# You'll be prompted to approve it on first use
```

**Option 2: Manual setup (User-scoped)**
```bash
# From the redstack-vault directory
claude mcp add --transport stdio --scope user redstack-vault \
  -- "$(pwd)/.mcp-server/start-stdio.sh"
```

**Usage:**
```bash
# In any Claude Code session, use /mcp to check server status
/mcp

# The same 10 tools are available automatically
# Example: "Show me all mimikatz commands"
```

**Logs:** Activity is logged to `.mcp-server/mcp-server-stdio.log`

### Other MCP Clients

Any MCP-compatible client can connect via:
- **SSE endpoint**: `http://localhost:3000/sse`
- **Protocol**: MCP over SSE transport
- **Tools**: 9 available

## 🛠️ Available Tools

1. **get_attack_chain_with_commands** - Get complete attack chain with all commands
2. **list_attack_chains** - List all available attack chains
3. **search_attack_chains** - Search attack chains by filters
4. **find_commands_by_tool** - Find commands using specific tools (mimikatz, nmap, etc.)
5. **find_commands_by_capability** - Semantic search by capability
6. **find_attack_chains_by_tool** - Find chains that use a specific tool
7. **list_available_tools** - List all indexed tools (35+)
8. **search_procedures** - Search by tactic, technique, platform
9. **get_vault_stats** - Get vault statistics

## 🎯 Example Queries

Once connected to AnythingLLM or Claude:

```
"Show me all attack chains that use mimikatz"
"Find commands for privilege escalation on Windows"
"Get the Kerberoast attack chain with all commands"
"List all available red team tools"
"Search for procedures related to credential dumping"
```

## 📝 Logging

All server activity is logged to `mcp-server.log` in the same directory. The log includes:

- **HTTP requests/responses** - Method, path, client IP, headers, status codes
- **SSE connections** - Client connections, disconnections, session lifecycle
- **Tool calls** - Tool name, arguments, response previews
- **Errors** - Any failures or exceptions
- **Vault operations** - Startup, data loading, statistics

### Log Format

```
2025-11-02 13:20:18 | INFO     | Method: GET
2025-11-02 13:20:18 | INFO     | Path: /health
2025-11-02 13:20:18 | INFO     | Client: 127.0.0.1
2025-11-02 13:20:18 | INFO     | Response Status: 200
```

### View Live Logs

```bash
# Follow the log in real-time
tail -f mcp-server.log

# View recent entries
tail -100 mcp-server.log

# Search for specific tool calls
grep "TOOL CALL" mcp-server.log

# Clear old logs
rm mcp-server.log
```

## 🔧 Configuration

### Custom Port

```bash
MCP_PORT=8000 ./start.sh
```

### Custom Vault Location

The script auto-detects the vault from `../` (parent directory). To override:

```bash
VAULT_PATH=/custom/path ./start.sh
```

## 📁 Directory Structure

```
output/
├── .mcp-server/            # MCP server (this directory)
│   ├── start.sh            # Start script (SSE transport)
│   ├── start-stdio.sh      # Start script (stdio transport for Claude Code)
│   ├── mcp_server.py       # Core vault interface
│   ├── mcp_server_sse.py   # SSE transport server
│   ├── mcp_server_stdio.py # stdio transport server
│   ├── .venv/              # Python virtual env (auto-created)
│   └── README.md           # This file
├── procedures/             # TTP procedures
├── commands/               # Executable commands
├── attack-chains/          # Multi-step attack chains
└── techniques/             # MITRE ATT&CK techniques
```

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Check what's using port 3000
lsof -i :3000

# Kill the process or use different port
MCP_PORT=8000 ./start.sh
```

### Python Not Found

Install Python 3.9+:
- macOS: `brew install python3`
- Linux: `apt install python3` or `yum install python3`
- Windows: Download from python.org

### Dependencies Won't Install

```bash
# Manually install in the venv
source .venv/bin/activate
pip install --upgrade pip
pip install mcp starlette uvicorn pyyaml
```

## 🔒 Security Note

This server runs **locally only** by default (localhost). It does not:
- Send data to external services
- Require API keys
- Store or transmit credentials

The vault data is read-only from markdown files.

## 📊 Performance

- **Startup time**: 2-3 seconds (loads entire vault into memory)
- **Query time**: <100ms for most operations
- **Memory usage**: ~50-100MB
- **Concurrent connections**: Unlimited (tested with 10+ clients)

## 🤝 Contributing

This MCP server is part of the Redstack project. Improvements welcome!

## 📝 License

Same license as the parent Redstack project.
