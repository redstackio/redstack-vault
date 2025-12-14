---
url: null
tags:
  - reverse-engineering
  - binary
type: tool
platforms:
  - Windows
  - Linux
description: Tool for searching strings in binary files.
id: 44bbaa60-dcf1-4374-91db-3959bb673b50
created_at: '2025-12-14T00:11:25.267Z'
updated_at: '2025-12-14T00:11:25.267Z'
verified: false
validated: true
submitted: true
---
# Binary Grep

**Status**: Unverified

## Overview

Used to search for strings like Steam URIs in binary files during reverse engineering.

## Description

Command-line tool for binary string searches.

## Features

- String searching in binaries

## Installation

### Requirements

- Unix-like system

### Install Commands

```bash
apt install binutils  # or similar
```

## Basic Usage

```bash
grep -a 'steam://' file.bin
```

### Common Options

| Option | Description |
|--------|-------------|
| -a | Treat as text |

## Examples

### Example 1: Basic Usage

Search Steam binaries.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Network Information]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- File access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Vim]]

## References

- Grep documentation
