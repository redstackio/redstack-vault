---
id: t1h2i3j4-k5l6-0124-hijk-8901234567
url: 'https://www.info-zip.org/'
tags:
  - archiving
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:27.867Z'
validated: true
submitted: true
---
# zip

**Status**: Unverified

## Overview

The 'zip' command-line tool is used for creating ZIP archives, commonly in security testing to craft malicious payloads with path traversal for vulnerabilities like directory traversal in unzip functions.

## Description

Zip compresses and archives files, supporting options for adding entries with custom paths. In offensive security, it's used to build exploit ZIPs for web app flaws, such as WordPress unzip_file path traversal.

## Features

- Feature 1: Path specification for entries, enabling traversal
- Feature 2: Compression and recursion for complex archives
- Feature 3: Symlink support for advanced payloads

## Installation

### Requirements

- Standard on most Unix-like systems

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt install zip
```

## Basic Usage

```bash
zip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -r | Recursive add |
| -q | Quiet mode |

## Examples

### Example 1: Basic Usage

```bash
zip archive.zip file.txt
```

### Example 2: Advanced Usage

```bash
zip malicious.zip ../../../../tmp/shell.php
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor process creation for 'zip' with suspicious paths
- Log archive creations in temp directories

## Related Procedures

- [[procedures/Craft-Malicious-Zip-with-Path-Traversal]]

## Related Tools

- [[unzip]]

## References

- Official documentation: https://www.info-zip.org/doc/zip.html
