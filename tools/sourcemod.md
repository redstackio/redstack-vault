---
url: 'https://wiki.alliedmods.net/Installing_sourcemod'
tags:
  - modding
  - csgo
  - plugin
type: tool
platforms:
  - Windows
  - Linux
description: Server modification framework for Source engine games
id: 6d109ecc-f5fc-48db-a0a9-36503555d57f
created_at: '2025-12-14T00:11:25.197Z'
updated_at: '2025-12-14T00:11:25.197Z'
verified: false
validated: true
submitted: true
---
# SourceMod

**Status**: Unverified

## Overview

Extends Source engine servers with scripting and plugins, used here for custom kick commands in CS:GO exploits.

## Description

Enables creation of plugins like testkick.smx for delivering XSS payloads without limits.

## Features

- Plugin system
- Scripting API
- Event hooking

## Installation

### Requirements

- Metamod
- Dedicated server

### Install Commands

```bash
# Download and extract to addons/sourcemod
```

## Basic Usage

```bash
sm plugins list
```

### Common Options

| Option | Description |
|--------|-------------|
| `sm` | Admin command prefix |

## Examples

### Example 1: Basic Usage

```bash
sm_kick
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Plugin installation logs
- Custom command execution

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/metamod]]

## References

- AlliedMods Wiki
