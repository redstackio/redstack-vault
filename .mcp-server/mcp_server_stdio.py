#!/usr/bin/env python3
"""
MCP Server with stdio Transport using official SDK

This uses the official @modelcontextprotocol SDK for Python to properly
implement the MCP protocol over stdio transport for Claude Code and other clients.

Usage:
    export VAULT_PATH=$(pwd)/output
    python3 mcp_server_stdio.py
"""

import os
import json
import asyncio
import logging
from typing import Any
from datetime import datetime

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from mcp_server import RedstackVault

# Setup logging
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, 'mcp-server-stdio.log')

# Create custom formatter for clean, readable logs
class CleanFormatter(logging.Formatter):
    def format(self, record):
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        level = record.levelname.ljust(8)
        return f"{timestamp} | {level} | {record.getMessage()}"

# Configure logging for our custom logger
logger = logging.getLogger('mcp_server')
logger.setLevel(logging.INFO)

# Also enable MCP SDK's internal logger
mcp_logger = logging.getLogger('mcp')
mcp_logger.setLevel(logging.DEBUG)

# File handler
fh = logging.FileHandler(log_file, mode='a', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(CleanFormatter())
logger.addHandler(fh)

# Console handler for errors only (stdio needs clean stdin/stdout)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)  # Only errors to console to avoid polluting stdio
ch.setFormatter(CleanFormatter())
logger.addHandler(ch)

# Add same handlers to MCP SDK logger
mcp_logger.addHandler(fh)
mcp_logger.addHandler(ch)

def log_separator(title=""):
    """Log a visual separator."""
    if title:
        logger.info(f"{'='*80}")
        logger.info(f"  {title}")
        logger.info(f"{'='*80}")
    else:
        logger.info(f"{'-'*80}")

# Initialize vault - default to parent directory of .mcp-server
if os.getenv('VAULT_PATH'):
    vault_path = os.getenv('VAULT_PATH')
else:
    # Vault is one directory up from .mcp-server
    vault_path = os.path.join(script_dir, '..')

log_separator("SERVER STARTUP (stdio)")
logger.info(f"Loading Redstack vault from: {vault_path}")
vault = RedstackVault(vault_path)
stats = vault.get_stats()
logger.info(f"Vault loaded successfully")
logger.info(f"  Procedures: {stats['procedures']}")
logger.info(f"  Commands: {stats['commands']}")
logger.info(f"  Attack Chains: {stats['attack_chains']}")
logger.info(f"  Verified Procedures: {stats['verified_procedures']}")
logger.info(f"  Verified Chains: {stats['verified_chains']}")
logger.info(f"Log file: {log_file}")
log_separator()

# Create MCP server
mcp_server = Server("redstack-vault")


@mcp_server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available MCP tools."""
    return [
        Tool(
            name="get_attack_chain_with_commands",
            description="Get a complete attack chain with all commands ready for execution. Returns expanded steps with commands, executors, tactics, and techniques. Perfect for automated execution.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the attack chain"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="list_attack_chains",
            description="List all available attack chain names in the vault",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="search_attack_chains",
            description="Search attack chains with filters like query, verified status, skill level, impact level, or complexity",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Text search in name, description, or tags"
                    },
                    "verified": {
                        "type": "boolean",
                        "description": "Filter by verified status"
                    },
                    "skill_level": {
                        "type": "string",
                        "description": "Filter by skill level (Beginner, Intermediate, Advanced)"
                    },
                    "impact_level": {
                        "type": "string",
                        "description": "Filter by impact level (LOW, MEDIUM, HIGH)"
                    }
                }
            }
        ),
        Tool(
            name="find_commands_by_tool",
            description="Find all commands that use a specific tool (e.g., mimikatz, nmap, metasploit)",
            inputSchema={
                "type": "object",
                "properties": {
                    "tool_name": {
                        "type": "string",
                        "description": "The name of the tool (e.g., 'mimikatz', 'nmap')"
                    }
                },
                "required": ["tool_name"]
            }
        ),
        Tool(
            name="find_commands_by_capability",
            description="Find commands by what they can do (semantic search). Examples: 'dump credentials', 'scan ports', 'privilege escalation'",
            inputSchema={
                "type": "object",
                "properties": {
                    "capability": {
                        "type": "string",
                        "description": "What you want to do (e.g., 'dump credentials', 'scan network')"
                    },
                    "platform": {
                        "type": "string",
                        "description": "Optional platform filter (Windows, Linux, macOS)"
                    }
                },
                "required": ["capability"]
            }
        ),
        Tool(
            name="find_attack_chains_by_tool",
            description="Find attack chains that use a specific tool",
            inputSchema={
                "type": "object",
                "properties": {
                    "tool_name": {
                        "type": "string",
                        "description": "The tool name to search for"
                    }
                },
                "required": ["tool_name"]
            }
        ),
        Tool(
            name="list_available_tools",
            description="List all tools indexed in the vault (35+ tools including mimikatz, nmap, metasploit, etc.)",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="search_procedures",
            description="Search procedures with filters for tactic, technique, platform, or verified status",
            inputSchema={
                "type": "object",
                "properties": {
                    "tactic": {
                        "type": "string",
                        "description": "MITRE ATT&CK tactic (e.g., 'Credential Access')"
                    },
                    "technique": {
                        "type": "string",
                        "description": "MITRE ATT&CK technique ID (e.g., 'T1003')"
                    },
                    "platform": {
                        "type": "string",
                        "description": "Target platform (Windows, Linux, macOS, Cloud)"
                    },
                    "verified": {
                        "type": "boolean",
                        "description": "Filter by verified status"
                    }
                }
            }
        ),
        Tool(
            name="text_search_procedures",
            description="Text search procedures across name, description, tags, tactics, techniques. Use this for keyword searches like 'XSS', 'SQL injection', 'privilege escalation'",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search text (searches in name, description, tags, tactics, techniques)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results (default: 20)",
                        "default": 20
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_vault_stats",
            description="Get statistics about the vault (procedures, commands, attack chains, verified content)",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]


@mcp_server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Execute a tool call."""
    log_separator("TOOL CALL REQUEST")
    logger.info(f"Tool: {name}")
    logger.info(f"Arguments: {json.dumps(arguments, indent=2)}")

    try:
        if name == "get_attack_chain_with_commands":
            result = vault.get_attack_chain_with_commands(arguments["name"])

        elif name == "list_attack_chains":
            result = vault.list_attack_chains()

        elif name == "search_attack_chains":
            result = vault.search_attack_chains(**arguments)

        elif name == "find_commands_by_tool":
            result = vault.find_commands_by_tool(arguments["tool_name"])

        elif name == "find_commands_by_capability":
            result = vault.find_commands_by_capability(
                arguments["capability"],
                arguments.get("platform", "")
            )

        elif name == "find_attack_chains_by_tool":
            result = vault.find_attack_chains_by_tool(arguments["tool_name"])

        elif name == "list_available_tools":
            result = vault.list_available_tools()

        elif name == "search_procedures":
            result = vault.search_procedures(**arguments)

        elif name == "text_search_procedures":
            result = vault.text_search_procedures(
                arguments["query"],
                arguments.get("limit", 20)
            )

        elif name == "get_vault_stats":
            result = vault.get_stats()

        else:
            result = {"error": f"Unknown tool: {name}"}

        # Log response
        response_preview = json.dumps(result, indent=2)[:500]  # First 500 chars
        logger.info(f"Response preview: {response_preview}...")

        if isinstance(result, list):
            logger.info(f"Response: Returned {len(result)} items")
        elif isinstance(result, dict):
            logger.info(f"Response: Dictionary with {len(result)} keys")

        log_separator()

        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    except Exception as e:
        logger.error(f"Tool call failed: {str(e)}")
        log_separator()
        return [TextContent(type="text", text=json.dumps({"error": str(e)}, indent=2))]


async def main():
    """Main entry point for stdio server."""
    log_separator("STDIO SERVER STARTING")
    logger.info("MCP Server ready for stdio communication")
    logger.info(f"Vault: {vault_path}")
    logger.info(f"Stats: {vault.get_stats()}")
    log_separator()

    async with stdio_server() as (read_stream, write_stream):
        await mcp_server.run(
            read_stream,
            write_stream,
            mcp_server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
