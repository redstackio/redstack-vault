---
url: null
tags:
  - pattern-search
  - credential-extraction
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Command-line utility for searching plain-text data sets for lines matching a
  regular expression.
id: 3e032f13-5175-4776-99e6-fc869aac9c2f
created_at: '2025-12-11T03:47:59.561Z'
updated_at: '2025-12-11T03:47:59.561Z'
verified: false
validated: true
submitted: true
---
# grep

**Status**: Unverified

## Overview

grep is a standard Unix command-line tool used to search and extract data from files based on patterns, commonly employed in security for parsing logs or extracted files for credentials.

## Description

It supports regular expressions and is ideal for post-exploitation data mining, such as finding usernames and passwords in VPN cache files.

## Features

- Regex pattern matching
- File searching and output redirection
- Recursive directory search

## Installation

### Requirements

- Available on most Unix-like systems

### Install Commands

```bash
# Typically pre-installed; on Windows, use Git Bash or install via package manager
```

## Basic Usage

```bash
grep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-E` | Extended regex |
| `-r` | Recursive search |

## Examples

### Example 1: Basic Usage

```bash
grep 'password' file.txt
```

### Example 2: Advanced Usage

```bash
grep -E 'username|password' /path/to/file
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor command-line executions in logs
- Detect unusual file access patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/download.py]]

## References

- GNU grep documentation
