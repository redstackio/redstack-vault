---
id: tool-sourcemod-001
url: 'https://wiki.alliedmods.net/Installing_sourcemod'
tags:
  - mod
  - server
  - csgo
type: tool
verified: false
platforms:
  - Windows
  - Game
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.809Z'
validated: true
submitted: true
---
# SourceMod

**Status**: Unverified

## Overview

SourceMod is a server-side mod framework for Source engine games like CS:GO, used to extend functionality with plugins for custom commands, event hooks, and actions like kicking players with payloads.

## Description

It provides SourcePawn scripting for plugins, enabling attackers to implement custom kick logic without message limits, facilitating XSS payload delivery in UI popups for RCE.

## Features

- Feature 1: Plugin API for event hooking (e.g., player_spawn)
- Feature 2: Custom console commands (e.g., sm_testkick)
- Feature 3: KickClient function for arbitrary messages

## Installation

### Requirements

- Metamod installed
- CS:GO dedicated server

### Install Commands

```bash
# Download and extract to csgo/addons/sourcemod
# Configure plugins.cfg to load .smx files
```

## Basic Usage

```bash
# In server console
sm plugins load testkick
```

### Common Options

| Option | Description |
|--------|-------------|
| sm_reload | Reload plugins |
| sm plugins list | List loaded plugins |

## Examples

### Example 1: Basic Usage

```bash
sm_kick #1 "message"
```

### Example 2: Advanced Usage

Develop plugin and load:

```bash
# Compile SourcePawn to .smx, place in plugins/
sm plugins load autokick
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[External Remote Services]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Check addons/sourcemod/plugins for .smx files
- Monitor sm_ prefixed console commands

## Related Procedures


## Related Tools

- [[tools/Metamod]]

## References

- https://wiki.alliedmods.net/Installing_sourcemod
