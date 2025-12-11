---
url: null
tags:
  - text-search
  - credential-extraction
type: tool
platforms:
  - Linux
  - macOS
description: >-
  Standard Unix utility for searching plain-text data sets for lines matching a
  regular expression.
id: 4e7d28d4-59c2-4202-864a-c3b3d02a7d21
created_at: '2025-12-11T06:10:40.257Z'
updated_at: '2025-12-11T06:10:40.257Z'
verified: false
validated: true
submitted: true
---
# grep

**Status**: Unverified

## Overview

grep is a command-line tool used to search for specific patterns in files, commonly employed in security for extracting data like credentials from dumped files.

## Description

It processes text using regular expressions to find and output matching lines, useful in post-exploitation for parsing large data sets.

## Features

- Regular expression support
- File and recursive searching
- Output formatting options

## Installation

### Requirements

- Standard on most Unix-like systems

### Install Commands

```bash
# Typically pre-installed; install via package manager if needed
apt install grep
```

## Basic Usage

```bash
grep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-E` | Extended regular expressions |
| `-r` | Recursive search |

## Examples

### Example 1: Basic Usage

```bash
grep 'password' file.txt
```

### Example 2: Advanced Usage

```bash
grep -E 'username|password' /path/to/file.mdb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitoring for grep commands in process logs
- Anomalous file access patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[awk]]
- [[sed]]

## References

- GNU grep documentation
