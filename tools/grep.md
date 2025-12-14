---
id: tool-grep-001
url: null
tags:
  - search
  - static-analysis
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.522Z'
validated: true
submitted: true
---
# grep

**Status**: Unverified

## Overview

Grep is a command-line utility for searching text patterns in files, ideal for locating vulnerable code snippets in source code.

## Description

Used in security testing to find functions like 'strcpy' or 'glob_url' in curl source, aiding XSS vulnerability discovery.

## Features

- Feature 1: Recursive directory searching
- Feature 2: Line number output for precise location
- Feature 3: Pattern matching with regex support

## Installation

### Requirements

- Standard on Unix-like systems

### Install Commands

```bash
# Pre-installed on Linux
```

## Basic Usage

```bash
grep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r, --recursive` | Recursive search |
| `-n` | Show line numbers |
| `-i` | Ignore case |

## Examples

### Example 1: Basic Usage

```bash
grep -rn "glob_url" src/
```

### Example 2: Advanced Usage

```bash
grep -rnw "strcpy" src/ | grep url
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process listings showing grep on source dirs
- Log entries for file access patterns

## Related Procedures

- [[procedures/Static-Code-Analysis-for-Vulnerable-URL-Handling]]

## Related Tools

- [[tools/git]]
- [[tools/curl]]

## References

- Man page: `man grep`
