---
url: null
tags:
  - archive
  - compression
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Command-line utility for creating and extracting tar archives, often used in
  handling GitLab project exports and imports.
id: 8477bb84-2465-4aab-9086-dff8fa992cfe
created_at: '2025-12-11T06:10:28.846Z'
updated_at: '2025-12-11T06:10:28.846Z'
verified: false
validated: true
submitted: true
---
# tar

**Status**: Unverified

## Overview

tar is a standard Unix utility for archiving files into tarballs, commonly used in security testing for handling compressed archives like GitLab project exports.

## Description

tar creates, extracts, and manipulates tape archive files, supporting compression with gzip. In offensive security, it's used for repackaging modified files in exploits involving file imports.

## Features

- Feature 1: Archive creation and extraction
- Feature 2: Compression integration (gzip, bzip2)
- Feature 3: Verbose output for debugging

## Installation

### Requirements

- Unix-like operating system
- Pre-installed on most distributions

### Install Commands

```bash
# Typically pre-installed; if not:
sudo apt install tar  # Debian/Ubuntu
```

## Basic Usage

```bash
tar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
tar -zcvf archive.tar.gz files/
```

### Example 2: Advanced Usage

```bash
tar -zxvf archive.tar.gz -C output_dir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual tar commands in logs
- Detection method 2: Audit file creation in sensitive directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[zip]]
- [[gzip]]

## References

- Official GNU tar documentation
- Man pages: man tar
