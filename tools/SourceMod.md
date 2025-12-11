---
url: 'https://wiki.alliedmods.net/Installing_sourcemod'
tags:
  - plugin
  - server
type: tool
platforms:
  - Windows
description: Server administration framework for Source engine games.
id: 5266cd8e-c581-4677-9100-8c3b31cfda08
created_at: '2025-12-11T06:10:15.635Z'
updated_at: '2025-12-11T06:10:15.635Z'
verified: false
validated: true
submitted: true
---
# SourceMod

**Status**: Unverified

## Overview

SourceMod is a plugin framework for Source engine games like CS:GO, allowing custom server modifications including kick plugins.

## Description

Used to install and run plugins like testkick.smx and autokick.smx for delivering XSS payloads in kick messages.

## Features

- Plugin loading
- Event hooking
- Custom commands

## Installation

### Requirements

- Metamod
- Dedicated server

### Install Commands

```bash
# Follow wiki instructions
```

## Basic Usage

```bash
sm plugins list
```

### Common Options

| Option | Description |
|--------|-------------|
| `sm_kick` | Kick player |

## Examples

### Example 1: Basic Usage

```bash
sm_kick <player>
```

### Example 2: Advanced Usage

```bash
sm_testkick <payload>
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Server log analysis
- Plugin monitoring

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metamod]]

## References

- https://wiki.alliedmods.net/Installing_sourcemod
