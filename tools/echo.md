---
id: tool-echo-2023
url: 'https://www.gnu.org/software/coreutils/echo'
tags:
  - output
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.844Z'
validated: true
submitted: true
---
# echo

**Status**: Unverified

## Overview

Echo prints arguments to standard output, used here to generate the exploit payload with hex escapes for CRLF.

## Description

Built-in shell command for crafting strings, including binary data via -e and \x escapes.

## Features

- Feature 1: Variable expansion
- Feature 2: Escape sequences
- Feature 3: No trailing newline with -n

## Installation

### Requirements

- Core shell utility

### Install Commands

Pre-installed.

## Basic Usage

```bash
echo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e` | Enable escapes |
| `-n` | No newline |

## Examples

### Example 1: Basic Usage

```bash
echo "hello"
```

### Example 2: Advanced Usage

```bash
echo -en "GET / HTTP/1.1\r\nHost: longstring:\r\n\r\n"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Rarely monitored; look for piped outputs in exploits

## Related Procedures

- [[procedures/Trigger-Squid-Host-Header-Buffer-Overflow]]

## Related Tools

- [[tools/printf]]

## References

- Man page: echo(1)
