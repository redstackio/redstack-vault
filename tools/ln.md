---
id: efdfc721-3c9b-4ec2-a82a-8683dd7c26c6
type: tool
verified: false
created_at: '2025-12-11T03:48:05.884Z'
updated_at: '2025-12-11T03:48:05.884Z'
platforms:
  - Linux
tags:
  - symlink
url: ''
description: Command-line tool for creating links
validated: true
submitted: true
---

# ln

**Status**: Unverified

## Overview

ln is a Unix command for creating hard or symbolic links between files, commonly used in exploits involving path traversal or symlink attacks.

## Description

This tool creates symbolic links that can point to sensitive files, allowing exploitation of vulnerabilities where links are followed, such as in archive extractions.

## Features

- Feature 1: Create symbolic links with -s
- Feature 2: Force creation with -f
- Feature 3: Create backups with --backup

## Installation

### Requirements

- Linux or Unix-like system

### Install Commands

```bash
# Built-in on most systems
```

## Basic Usage

```bash
ln --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-s` | Create symbolic link |
| `-f` | Force |

## Examples

### Example 1: Basic Usage

```bash
ln -s target link
```

### Example 2: Advanced Usage

```bash
ln -sf target link
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor symlink creations
- Audit links in uploaded archives

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #mkdir
- #tar

## References

- man ln
