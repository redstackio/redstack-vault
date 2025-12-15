---
id: 123e4567-e89b-12d3-a456-426614174016
name: mkdir
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.148Z'
platforms:
  - Linux
  - macOS
  - Windows (via Git Bash)
tags:
  - directory-creation
url: null
validated: true
submitted: true
---

# mkdir

**Status**: Unverified

## Overview

mkdir is a Unix command to create directories, essential for setting up isolated environments in security testing and exploitation workflows.

## Description

Used to prepare test directories before running vulnerable tools, ensuring operations are contained and verifiable.

## Features

- Feature 1: Create single or multiple directories
- Feature 2: Parent directory creation with -p
- Feature 3: Permission setting with -m

## Installation

### Requirements

- Standard on Unix-like systems

### Install Commands

```bash
# Pre-installed
```

## Basic Usage

```bash
mkdir --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Create parents as needed |
| -m | Set permissions |

## Examples

### Example 1: Basic Usage

```bash
mkdir tests
```

### Example 2: Advanced Usage

```bash
mkdir -p tests/subdir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Log directory creation events
- Alert on unusual directory names in sensitive paths

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: mktemp]]

## References

- Man page: man mkdir
