---
url: ''
tags:
  - reverse-engineering
type: tool
platforms:
  - Linux
  - Windows
description: Tool for searching strings in binary files.
id: 9a9be603-efe3-47ef-9870-6125f1eb8ca3
created_at: '2025-12-11T06:10:17.459Z'
updated_at: '2025-12-11T06:10:17.459Z'
verified: false
validated: true
submitted: true
---
# Binary Grep

**Status**: Unverified

## Overview

Binary grep searches for strings in executable files, useful for reverse engineering.

## Description

Used to find Steam URI patterns in the Steam binary.

## Features

- String searching in binaries
- Pattern matching

## Installation

### Requirements

- Unix-like system

### Install Commands

```bash
# Typically 'grep' with options or 'strings'
```

## Basic Usage

```bash
grep -a 'steam://' steam.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `-a` | Process as text |

## Examples

### Example 1: Basic Usage

```bash
grep -a 'steam://' steam.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[User Execution]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- File access logs on binaries

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

- Man page for grep
