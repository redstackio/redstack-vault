---
url: ''
tags:
  - inspection
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.329Z'
id: 0b310116-afdd-4c7b-a687-c9928ec9c953
validated: true
submitted: true
---
# cat

**Status**: Unverified

## Overview

cat concatenates and displays file contents, used to inspect cached, overwritten, or template files post-exploit.

## Description

Simple tool for viewing text files; no editing. Key for verifying exploit success by reading file contents.

## Features

- Feature 1: Multiple files at once
- Feature 2: Number lines (-n)
- Feature 3: End-of-line show (-e)

## Installation

### Requirements

- Built-in

### Install Commands

N/A

## Basic Usage

```bash
cat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -n | Number lines |
| -e | Show ends |

## Examples

### Example 1: Basic Usage

```bash
cat public/books/1.html
```

### Example 2: Advanced Usage

```bash
cat -n README.md
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Audit logs for file reads

## Related Procedures

- [[procedures/Exploit-Directory-Traversal-for-Arbitrary-File-Writing]]

## Related Tools

- [[tools/type]] (alternative)

## References

- Man page: man cat
