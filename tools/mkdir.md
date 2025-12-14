---
id: tool-uuid-3
url: null
tags:
  - filesystem
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.322Z'
validated: true
submitted: true
---
---

# mkdir

**Status**: Unverified

## Overview

Mkdir is a Unix command to create directories, essential for structuring attack artifacts like maliciously named folders in XSS exploits.

## Description

Used here to create directories with embedded JS payloads, exploiting name rendering in web servers.

## Features

- Feature 1: Create single or nested directories
- Feature 2: Set permissions
- Feature 3: Verbose output option

## Installation

### Requirements

- Standard Unix tool

### Install Commands

```bash
# Pre-installed
mkdir --help
```

## Basic Usage

```bash
mkdir --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Create parents, no error if exists |
| `-v` | Verbose |

## Examples

### Example 1: Basic Usage

```bash
mkdir dir
```

### Example 2: Advanced Usage

```bash
mkdir -p '><payload>'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Log mkdir with anomalous names
- EDR alerts on dir creations

## Related Procedures


## Related Tools

- [[tools/touch]]

## References

- Man page: man mkdir

