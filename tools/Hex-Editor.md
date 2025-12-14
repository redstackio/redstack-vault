---
id: tool-hex-editor-001
url: ''
tags:
  - binary-edit
  - file-modification
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.396Z'
validated: true
submitted: true
---
# Hex-Editor

**Status**: Unverified

## Overview

A hex editor is a tool for viewing and editing the hexadecimal representation of binary files, used here to modify embedded URLs in AVI files without corrupting structure.

## Description

Commonly used in exploit development to craft malicious files; examples include HxD (Windows), hexedit (Linux), or bless (macOS). Allows precise byte-level changes for embedding HLS URLs in GAB2 chunks.

## Features

- Feature 1: Binary search and replace for strings like HTTP URLs
- Feature 2: Offset navigation to locate subtitle chunks
- Feature 3: File validation to ensure edits don't break AVI format

## Installation

### Requirements

- Standard OS package manager

### Install Commands

```bash
# Linux (hexedit)
sudo apt install hexedit

# Windows: Download HxD from mh-nexus.de
```

## Basic Usage

```bash
hexedit http_q.avi
```

### Common Options

| Option | Description |
|--------|-------------|
| Search | Find string in binary |
| Edit | Overwrite bytes |
| Save | Write changes to file |

## Examples

### Example 1: Basic Usage

```bash
hexedit modified.avi
```
Search for 'http://example.com', replace with attacker URL.

### Example 2: Advanced Usage

Use GUI like HxD: Open file, go to offset, edit URL, save.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Develop Capabilities]] Develop Capabilities

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- File modification timestamps on crafted binaries
- Anomalous hex patterns in uploaded media

## Related Procedures

- [[procedures/Craft-Malicious-AVI-for-SSRF]]
- [[procedures/Execute-Local-File-Disclosure-via-AVI]]

## Related Tools

- [[tools/gen_avi.py]]

## References

- HxD: https://mh-nexus.de/en/hxd/
