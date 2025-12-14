---
url: 'https://www.sourcemm.net/'
tags:
  - modding
  - csgo
type: tool
platforms:
  - Windows
  - Linux
description: Meta plugin loader for Source engine servers
id: 711f034f-05da-4758-ad18-767d346d545b
created_at: '2025-12-14T00:11:25.195Z'
updated_at: '2025-12-14T00:11:25.195Z'
verified: false
validated: true
submitted: true
---
# Metamod

**Status**: Unverified

## Overview

Required base for SourceMod, enabling mod loading on CS:GO servers.

## Description

Loads extensions like SourceMod for advanced server modifications in exploits.

## Features

- Plugin loading
- API extensions

## Installation

### Requirements

- Dedicated server

### Install Commands

```bash
# Download and configure
```

## Basic Usage

```bash
meta list
```

### Common Options

| Option | Description |
|--------|-------------|
| `meta` | Command prefix |

## Examples

### Example 1: Basic Usage

```bash
meta load addons/sourcemod
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Server mod logs

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

- SourceMM Website
