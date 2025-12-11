---
url: >-
  https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers
tags:
  - server
  - hosting
type: tool
platforms:
  - Windows
description: 'Dedicated server software for hosting CS:GO games.'
id: 28c08a94-d68d-4a1f-9aed-a12fe53d0559
created_at: '2025-12-11T06:10:15.630Z'
updated_at: '2025-12-11T06:10:15.630Z'
verified: false
validated: true
submitted: true
---
# CS:GO Dedicated Server

**Status**: Unverified

## Overview

Official dedicated server for hosting CS:GO multiplayer games, used to test exploits.

## Description

Hosts servers where remote kick exploits and plugins can be tested against connecting clients.

## Features

- Multiplayer hosting
- Plugin support via Metamod/SourceMod

## Installation

### Requirements

- SteamCMD

### Install Commands

```bash
# Use SteamCMD to install
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

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to untrusted servers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/SourceMod]]

## References

- https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers
