---
url: 'https://www.sourcemm.net/'
tags:
  - plugin
  - loader
type: tool
platforms:
  - Windows
description: Plugin loader for Source engine servers.
id: 2ddf1e1b-4e7d-46ff-82f4-981b1a787016
created_at: '2025-12-11T06:10:15.632Z'
updated_at: '2025-12-11T06:10:15.632Z'
verified: false
validated: true
submitted: true
---
# Metamod

**Status**: Unverified

## Overview

Metamod is a plugin loader required for running SourceMod on dedicated Source engine servers.

## Description

Enables loading of SourceMod for custom functionality like kick plugins in CS:GO servers.

## Features

- Plugin management
- Compatibility layer

## Installation

### Requirements

- Dedicated server

### Install Commands

```bash
# Follow official instructions
```

## Basic Usage

```bash
meta list
```

### Common Options

| Option | Description |
|--------|-------------|
| `meta load` | Load plugin |

## Examples

### Example 1: Basic Usage

```bash
meta load sourcemod
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Server configuration checks

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

- https://www.sourcemm.net/
