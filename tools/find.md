---
url: ''
tags:
  - search
  - filesystem
type: tool
platforms:
  - Linux
  - macOS
description: File search utility
id: 012c8f80-3837-4756-ac99-2c0f69e6be96
created_at: '2025-12-11T03:47:39.613Z'
updated_at: '2025-12-11T03:47:39.613Z'
verified: false
validated: true
submitted: true
---
# find

**Status**: Unverified

## Overview

find searches for files in a directory hierarchy.

## Description

Used for locating files like authorized_keys during verification.

## Features

- Feature 1: Name-based search
- Feature 2: Type filtering
- Feature 3: Permission checks

## Installation

### Requirements

- Standard on Unix-like systems

### Install Commands

```bash
# Built-in
```

## Basic Usage

```bash
find --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-name` | Search by name |
| `-type` | File type |

## Examples

### Example 1: Basic Usage

```bash
find . -name '*.txt'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Command history logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #locate
- #grep

## References

- Man page: find(1)
