---
url: null
tags:
  - gaming
  - console
type: tool
platforms:
  - Windows
  - MacOS
  - Linux
description: >-
  In-game console for executing commands in Source Engine games like Left 4 Dead
  2
id: 12b84a11-64cb-4ff9-9008-19a49c96c771
created_at: '2025-12-11T03:46:01.587Z'
updated_at: '2025-12-11T03:46:01.587Z'
verified: false
validated: true
submitted: true
---
# Developer Console

**Status**: Unverified

## Overview

The Developer Console is an in-game tool in Source Engine games for executing commands, loading maps, and triggering functions, useful for testing and exploitation.

## Description

Enabled via game settings or launch options, it allows input of commands like 'map' to load assets, which can trigger vulnerabilities in parsing routines.

## Features

- Command execution: Run game-specific commands.
- Map loading: Load custom or malformed maps.
- Debugging output: View console logs.

## Installation

### Requirements

- Left 4 Dead 2 installed
- Launch option: -console

### Install Commands

```bash
# Launch game with console: Left4Dead2.exe -console
```

## Basic Usage

```bash
# In console: help
```

### Common Options

| Option | Description |
|--------|-------------|
| `map` | Load a map |
| `sv_cheats 1` | Enable cheats |

## Examples

### Example 1: Basic Usage

```bash
map c1m1_hotel
```

### Example 2: Advanced Usage

```bash
sv_cheats 1; map c1m1_hotel
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor console command logs for suspicious map loads.
- Detect enabling of developer mode in game configs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Debugger]]

## References

- Source Engine documentation: https://developer.valvesoftware.com/wiki/Developer_Console
