---
url: null
tags:
  - plugin
  - csgo
  - rce
type: tool
platforms:
  - Windows
  - 'CS:GO'
description: Custom SourceMod plugin for automatic kicking with exploits
id: 5cd3fdb7-5faf-4e18-8951-62b5510b6237
created_at: '2025-12-14T00:11:25.191Z'
updated_at: '2025-12-14T00:11:25.191Z'
verified: false
validated: true
submitted: true
---
# Autokick Smx

**Status**: Unverified

## Overview

SourceMod plugin for automatic kicking on player spawn with XSS payload for zero-interaction exploits.

## Description

Hooks player_spawned, delays with timer, and kicks with screen-filling payload.

## Features

- Event hooking
- Timed kicks
- Auto-exploit

## Installation

### Requirements

- SourceMod

### Install Commands

```bash
# Place in addons/sourcemod/plugins
```

## Basic Usage

```bash
# Automatic on spawn
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Automatic |

## Examples

### Example 1: Basic Usage

```bash
# Plugin runs automatically
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Spawn event monitoring

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

- Custom plugin code
