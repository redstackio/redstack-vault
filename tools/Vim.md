---
url: null
tags:
  - editor
  - reverse-engineering
type: tool
platforms:
  - Windows
  - Linux
description: Text editor for searching binary string tables.
id: 2d8562b5-13f8-464b-a7b0-7b25cdbf3c27
created_at: '2025-12-14T00:11:25.265Z'
updated_at: '2025-12-14T00:11:25.265Z'
verified: false
validated: true
submitted: true
---
# Vim

**Status**: Unverified

## Overview

Vim is used for searching and viewing string tables in binaries for undocumented URIs.

## Description

Powerful text editor with search capabilities.

## Features

- String searching
- Binary mode

## Installation

### Requirements

- Any OS

### Install Commands

```bash
apt install vim
```

## Basic Usage

```bash
vim file.bin
```

### Common Options

| Option | Description |
|--------|-------------|
| /search | Search string |

## Examples

### Example 1: Basic Usage

Search for 'steam://'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Network Information]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Binary-Grep]]

## References

- Vim official site
