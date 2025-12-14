---
id: t-install
type: tool
name: install
verified: false
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.726Z'
platforms:
  - Linux
tags:
  - file-management
url: ''
validated: true
submitted: true
---

# install

**Status**: Unverified

## Overview

The install utility is a standard Linux command for copying files and directories while setting specific permissions, ownership, and modes. Commonly used in security testing to create files with controlled access for vulnerability demonstrations.

## Description

Install allows precise control over file attributes during creation or copy, making it ideal for simulating secure environments. In offensive security, it's used to set up test files with strict permissions before exploiting tools that mishandle them, like libcurl.

## Features

- Feature 1: Set mode with -m (e.g., 600 for owner-only).
- Feature 2: Change ownership with -o and -g.
- Feature 3: Copy from special files like /dev/null for empty targets.

## Installation

### Requirements

- Standard on Linux distributions (part of coreutils).

### Install Commands

```bash
# Already installed on most systems
```

## Basic Usage

```bash
install --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m, --mode=MODE` | Set permission mode |
| `-o, --owner=OWNER` | Set owner |
| `-g, --group=GROUP` | Set group |

## Examples

### Example 1: Basic Usage

```bash
install -m 600 /dev/null testfile
```

### Example 2: Advanced Usage

```bash
install -m 644 -o user -g group source dest
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Log file creation events with specific modes.
- Monitor install invocations in process audits.

## Related Procedures

- [[procedures/Create-and-Verify-Secure-Cookie-Jar-File]]

## Related Tools

- [[tools/ls]]

## References

- Man page: man install
