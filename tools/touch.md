---
id: tool-003
url: null
tags:
  - file-utility
type: tool
verified: false
platforms:
  - macOS
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T03:16:02.736Z'
validated: true
submitted: true
---
# touch

**Status**: Unverified

## Overview

touch is a standard Unix command-line utility for creating empty files or updating timestamps, used here to create files with malicious names for XSS payloads.

## Description

In security contexts, touch allows rapid creation of files with special characters, enabling injection attacks like filename-based XSS in vulnerable servers.

## Features

- Feature 1: Create new empty files
- Feature 2: Update access/modification times
- Feature 3: Handle special characters with quoting

## Installation

### Requirements

- Unix-like OS (pre-installed on macOS)

### Install Commands

```bash
# Already available; check with
touch --help
```

## Basic Usage

```bash
touch --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -a | Change access time |
| -m | Change modification time |

## Examples

### Example 1: Basic Usage

```bash
touch file.txt
```

### Example 2: Advanced Usage

```bash
touch 'malicious"><script>alert(1)</script>'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Audit logs for file creations with anomalous names
- Filesystem monitoring for suspicious filenames

## Related Procedures

- [[procedures/Create-Malicious-Filename-for-XSS]]

## Related Tools

- [[New-Item]]

## References

- Man page: man touch
