---
id: tool-gnu-tar
name: tar
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.182Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - archiving
  - extraction
url: 'https://www.gnu.org/software/tar/'
validated: true
submitted: true
---

# tar

**Status**: Unverified

## Overview

GNU tar is a utility for archiving and extracting files, commonly used in security testing for handling compressed archives like GitLab's .tar.gz exports to inspect or modify contents such as symlinks and JSON files.

## Description

Tar creates and manipulates tar archives, supporting compression with gzip. In offensive security, it's used to extract application exports for credential hunting or to package payloads with symlinks for vulnerability testing, like preserving symlinks in GitLab import/export without dereferencing.

## Features

- Feature 1: Archive creation/extraction with options for compression (gzip, bzip2)
- Feature 2: Verbose listing to inspect contents, permissions, and symlinks
- Feature 3: Change directory (-C) for targeted extraction without full path pollution

## Installation

### Requirements

- POSIX-compliant system (Linux/macOS standard)

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install tar

# On macOS (pre-installed)
# No action needed

# On Windows (via Git Bash or WSL)
# Install via package manager
```

## Basic Usage

```bash
tar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -c | Create archive |
| -x | Extract archive |
| -z | Gzip compression |
| -v | Verbose output |
| -f | Specify file |
| -t | List contents |
| -C | Change to directory before operation |

## Examples

### Example 1: Basic Usage

```bash
tar -xzf archive.tar.gz
```
Extracts gzip tar to current dir.

### Example 2: Advanced Usage

```bash
tar -czf new_archive.tar.gz -C /source/dir .
```
Creates compressed archive from dir.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution (for payload packaging)
- [[Remote File Copy]] Ingress Tool Transfer (archiving tools/payloads)

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for tar executions with suspicious files (e.g., exports in /tmp)
- File system logs for archive creation/extraction in temp dirs
- Network logs if archives contain exfil data

## Related Procedures


## Related Tools

- [[zip]]
- [[7z]]

## References

- Official documentation: https://www.gnu.org/software/tar/manual/
- Related resources: Man pages (man tar)
