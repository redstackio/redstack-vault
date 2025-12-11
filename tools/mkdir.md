---
id: 3ca5fc5f-6130-42f4-b07e-4f7e460d1da0
type: tool
verified: false
created_at: '2025-12-11T03:48:05.886Z'
updated_at: '2025-12-11T03:48:05.886Z'
platforms:
  - Linux
tags:
  - directory-creation
url: ''
description: Command-line tool for creating directories
validated: true
submitted: true
---

# mkdir

**Status**: Unverified

## Overview

mkdir is a standard Unix command used to create new directories, essential for structuring files and payloads in security testing scenarios like preparing malicious archives.

## Description

This tool creates directories with specified names and permissions. In offensive security, it's used to organize exploit payloads, such as creating hashed directories for symlink exploits in tar files.

## Features

- Feature 1: Create single or multiple directories
- Feature 2: Set permissions with -m
- Feature 3: Create parent directories with -p

## Installation

### Requirements

- Linux or Unix-like system

### Install Commands

```bash
# Built-in on most systems, no installation needed
```

## Basic Usage

```bash
mkdir --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Create parent directories |
| `-m` | Set mode/permissions |

## Examples

### Example 1: Basic Usage

```bash
mkdir newdir
```

### Example 2: Advanced Usage

```bash
mkdir -p path/to/newdir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor filesystem changes
- Log directory creations in sensitive paths

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #ln
- #tar

## References

- man mkdir
