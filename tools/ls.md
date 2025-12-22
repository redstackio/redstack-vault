---
id: t-ls
type: tool
name: ls
verified: false
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.722Z'
platforms:
  - Linux
tags:
  - file-listing
  - recon
url: ''
validated: true
submitted: true
---

# ls

**Status**: Unverified

## Overview

ls is a core Linux command for listing directory contents, essential for inspecting file permissions, sizes, and metadata in security assessments and vulnerability verification.

## Description

In offensive security, ls is used to reconnaissance file states before and after exploits, particularly to check permission changes that could lead to disclosures. The -l option provides detailed views critical for confirming access controls.

## Features

- Feature 1: Long format (-l) for permissions and ownership.
- Feature 2: Recursive listing (-R) for directories.
- Feature 3: Human-readable sizes (-h).

## Installation

### Requirements

- Part of coreutils, pre-installed on Linux.

### Install Commands

```bash
# Standard installation
```

## Basic Usage

```bash
ls --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Long format details |
| `-a` | Show hidden files |
| `-h` | Human-readable sizes |

## Examples

### Example 1: Basic Usage

```bash
ls -l file.txt
```

### Example 2: Advanced Usage

```bash
ls -la /tmp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Common command, hard to detect alone; monitor in context with permission checks.
- Use syscall tracing for ls executions on sensitive paths.

## Related Procedures

- [[procedures/Create-and-Verify-Secure-Cookie-Jar-File]]
- [[procedures/Verify-Changed-File-Permissions]]

## Related Tools

- [[tools/install]]

## References

- Man page: man ls
