---
id: tool-echo-001
url: null
tags:
  - shell-builtin
  - output
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.540Z'
validated: true
submitted: true
---
# echo

**Status**: Unverified

## Overview

echo is a shell built-in command for outputting text or data, often used with escapes to generate binary files like images in testing scenarios.

## Description

As a core shell utility, echo interprets backslashes for hex/escape sequences, making it suitable for creating minimal files in security testing without additional tools.

## Features

- Feature 1: Basic text output
- Feature 2: Escape interpretation with -e
- Feature 3: Redirection to files for binary generation

## Installation

### Requirements

- Available in all POSIX-compliant shells (bash, zsh, etc.)

### Install Commands

```bash
# No installation needed; part of shell
```

## Basic Usage

```bash
echo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e` | Enable backslash escapes |
| `-n` | No trailing newline |

## Examples

### Example 1: Basic Usage

```bash
echo "Hello World"
```

### Example 2: Advanced Usage

```bash
echo -e "\x48\x65\x6c\x6c\x6f" > file.bin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Shell history showing echo with hex escapes
- File creation events for binary outputs
- Minimal process footprint; hard to detect standalone

## Related Procedures


## Related Tools

- [[printf]]

## References

- Bash manual: man echo
