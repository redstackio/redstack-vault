---
id: tool-metamod-001
url: 'https://www.sourcemm.net/'
tags:
  - mod
  - loader
  - csgo
type: tool
verified: false
platforms:
  - Windows
  - Game
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.799Z'
validated: true
submitted: true
---
# Metamod

**Status**: Unverified

## Overview

Metamod is a plugin loader for Source engine games like CS:GO, required to run frameworks like SourceMod for extending server capabilities with custom mods.

## Description

It acts as a base layer to inject DLLs and load plugins, essential for SourceMod's operation in delivering custom kick payloads via API calls in exploitation scenarios.

## Features

- Feature 1: DLL injection for mod support
- Feature 2: Configuration via metamod.vdf
- Feature 3: Compatibility with Source games

## Installation

### Requirements

- CS:GO dedicated server

### Install Commands

```bash
# Download from sourcemm.net, extract to csgo/addons/metamod
# Edit gameinfo.txt to include +host_thread_mode 2
```

## Basic Usage

```bash
# Server starts with metamod loaded automatically
meta version
```

### Common Options

| Option | Description |
|--------|-------------|
| meta load | Load a plugin |
| meta unload | Unload a plugin |

## Examples

### Example 1: Basic Usage

```bash
# In server console
meta list
```

### Example 2: Advanced Usage

Configure for SourceMod:

```bash
# In metamod.vdf
"Plugins"
{
	"addons/sourcemod/mm_sourcemod_core" "1"
}
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[External Remote Services]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of addons/metamod folder
- meta commands in logs

## Related Procedures


## Related Tools

- [[tools/SourceMod]]

## References

- https://www.sourcemm.net/
