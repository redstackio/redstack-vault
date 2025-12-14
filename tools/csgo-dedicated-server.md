---
url: >-
  https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers
tags:
  - gaming
  - server
  - csgo
type: tool
platforms:
  - Windows
  - Linux
description: 'Dedicated server for Counter-Strike: Global Offensive'
id: 02fe356a-6291-45e5-9ac6-70477d97131b
created_at: '2025-12-14T00:11:25.199Z'
updated_at: '2025-12-14T00:11:25.199Z'
verified: false
validated: true
submitted: true
---
# CS:GO Dedicated Server

**Status**: Unverified

## Overview

Official tool for hosting CS:GO servers, used to test kick functionality and deliver XSS payloads.

## Description

Allows setting up multiplayer servers, extensible with mods like SourceMod for custom exploits.

## Features

- Multiplayer hosting
- Console commands
- Plugin support

## Installation

### Requirements

- SteamCMD

### Install Commands

```bash
# Follow Valve wiki instructions
```

## Basic Usage

```bash
srcds -game csgo
```

### Common Options

| Option | Description |
|--------|-------------|
| `-port` | Server port |

## Examples

### Example 1: Basic Usage

```bash
srcds -game csgo -console
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual server traffic
- Malicious kick events

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sourcemod]]

## References

- Valve Developer Wiki
