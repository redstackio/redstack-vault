---
id: uuid-amx
url: 'https://www.amxmodx.org/'
tags:
  - server-mod
  - plugin-framework
  - gaming
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.431Z'
validated: true
submitted: true
---
# AMX-Mod-X

**Status**: Unverified

## Overview

AMX Mod X is a server-side modification framework for Half-Life-based games like Counter-Strike, enabling custom plugins to alter gameplay and network behavior, commonly used in exploit scenarios to send crafted messages.

## Description

It provides a scripting environment (Pawn language) for plugins that hook into game events, such as HUD initialization, allowing interception and modification of client-server communications. In offensive security, it's used to deploy PoC exploits targeting client parsers. Features include module loading, API for message sending, and compatibility with HLSDK.

## Features

- Feature 1: Plugin scripting in .sma files compiled to .amxx
- Feature 2: Hooks for net messages like WeaponList
- Feature 3: Server-side execution without client mods

## Installation

### Requirements

- Half-Life dedicated server
- Windows or Linux

### Install Commands

```bash
# Extract to cstrike/addons
# No specific command; manual copy of files
```

## Basic Usage

```bash
# Server auto-loads on startup
hlds.exe -game cstrike +map de_dust
```

### Common Options

| Option | Description |
|--------|-------------|
| -console | Enable console mode |
| -port 27015 | Bind to port |

## Examples

### Example 1: Basic Usage

Load plugins via plugins.ini.

### Example 2: Advanced Usage

Hook messages in plugin code: public client_connect(id) { ... }

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Log entries for amxmodx_mm module load
- Unusual plugin files in addons directory
- Anomalous net message traffic

## Related Procedures


## Related Tools

- [[tools/AMXX-Compiler]]

## References

- Official documentation: https://www.amxmodx.org/docs/
- HLSDK resources
