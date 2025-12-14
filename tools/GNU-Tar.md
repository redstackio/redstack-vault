---
url: 'https://www.gnu.org/software/tar/'
tags:
  - archiving
  - compression
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-25T00:00:00Z'
updated_at: '2025-12-14T17:24:08.325Z'
id: 27c9f778-c42a-44bc-8c2a-a48769d56929
validated: true
submitted: true
---
# GNU-Tar

**Status**: Unverified

## Overview

GNU Tar is a utility for archiving files into tar archives, often combined with gzip for .tar.gz format, used here for manipulating GitLab exports while preserving symlinks in security testing.

## Description

Tar handles creation, extraction, and listing of archives, crucial for inserting symlinks into GitLab exports without altering file permissions or structures. In offensive operations, it's used to craft malicious payloads for file read vulnerabilities.

## Features

- Feature 1: Symlink preservation during archiving
- Feature 2: Gzip integration for compression
- Feature 3: Verbose mode for inspection

## Installation

### Requirements

- Standard Unix-like system

### Install Commands

```bash
# On Ubuntu/Debian
apt install tar

# On macOS (pre-installed)

# On Windows (via WSL or Git Bash)
```

## Basic Usage

```bash
tar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c` | Create archive |
| `-x` | Extract archive |
| `-z` | Gzip filter |
| `-v` | Verbose |
| `-f` | File name |

## Examples

### Example 1: Basic Usage

```bash
tar -czvf archive.tar.gz directory/
```

### Example 2: Advanced Usage

```bash
tar -xzf archive.tar.gz
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for tar executions with unusual files
- Log archive creations in temp directories

## Related Procedures


## Related Tools

- [[7-Zip]]

## References

- Official documentation: https://www.gnu.org/software/tar/manual/
