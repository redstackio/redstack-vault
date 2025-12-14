---
id: tool-uuid-2
url: null
tags:
  - file-utils
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.066Z'
validated: true
submitted: true
---
# touch

**Status**: Unverified

## Overview

touch is a standard Unix command for creating empty files or updating timestamps, used here to create trigger files for vulnerability exploitation.

## Description

Part of coreutils, touch creates new files without content or modifies access/modification times. In security contexts, it's for setting up test artifacts like fake HTML files to trigger server behaviors.

## Features

- Feature 1: Create empty files
- Feature 2: Update timestamps
- Feature 3: Batch operations with wildcards

## Installation

### Requirements

- Unix-like OS

### Install Commands

```bash
# Pre-installed on Linux/macOS
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
touch -t 202301010000 file.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- File system audits for new empty files
- Command history logs

## Related Procedures

- [[procedures/Create-Trigger-HTML-File]]

## Related Tools

- [[cat]]
- [[echo]]

## References

- Man page: man touch
