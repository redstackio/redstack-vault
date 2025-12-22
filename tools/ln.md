---
id: tool-ln
url: 'https://man7.org/linux/man-pages/man1/ln.1.html'
tags:
  - file-system
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.609Z'
validated: true
submitted: true
---
# ln

**Status**: Unverified

## Overview

Unix command-line utility for creating hard or symbolic links between files, commonly used in security testing to set up symlink-based attacks like path traversal.

## Description

The `ln` tool manages file links in Unix-like systems. Symbolic links (-s) are pointers to other files or directories, enabling bypasses in vulnerable servers that don't validate paths. In offensive ops, it's used to create traversal aids without modifying targets.

## Features

- Feature 1: Create symbolic (-s) or hard links
- Feature 2: Support for relative/absolute paths
- Feature 3: Force overwrite with -f flag

## Installation

### Requirements

- Standard on Linux/macOS

### Install Commands

```bash
# Pre-installed; no action needed
```

## Basic Usage

```bash
ln --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-s` | Symbolic link |
| `-f` | Force overwrite |
| `-n` | No dereference |

## Examples

### Example 1: Basic Usage

```bash
ln -s target source
```

### Example 2: Advanced Usage

```bash
ln -sf ../../ symdir  # Force symlink creation
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor filesystem events for new symlinks (e.g., inotify or audit logs)
- Scan for suspicious links pointing to sensitive paths

## Related Procedures

- [[procedures/Create-Symbolic-Link-for-Path-Traversal]]

## Related Tools

- [[cp]] (for copying instead of linking)

## References

- Man page: https://man7.org/linux/man-pages/man1/ln.1.html
