---
id: fcdbbbf9-dd15-41b2-85e5-5ff7e1f1598a
name: mktemp
type: tool
verified: false
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.902Z'
platforms:
  - Linux
tags:
  - temp-files
  - setup
url: 'https://www.man7.org/linux/man-pages/man1/mktemp.1.html'
validated: true
submitted: true
---

# mktemp

**Status**: Unverified

## Overview

mktemp creates temporary files or directories with unique names, used in exploits to set up isolated environments without collisions.

## Description

In path traversal attacks, mktemp -d provides a safe temp dir for symlinks, ensuring exploit artifacts are contained.

## Features

- Feature 1: Secure random naming to avoid races
- Feature 2: Directory creation with -d
- Feature 3: Custom template support

## Installation

### Requirements

- Coreutils package

### Install Commands

```bash
apt install coreutils
```

## Basic Usage

```bash
mktemp --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d | Create directory |
| -t | Use template |

## Examples

### Example 1: Basic Usage

```bash
mktemp -d
```

### Example 2: Advanced Usage

```bash
temp=$(mktemp -d -t exploit.XXXXXX)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor mktemp calls in scripts for temp dirs used in exploits

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/bash]]
- [[tools/tmpfile]]

## References

- Man page: https://www.man7.org/linux/man-pages/man1/mktemp.1.html
