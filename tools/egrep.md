---
id: tool-002
url: 'https://www.gnu.org/software/grep/'
tags:
  - parsing
  - grep
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.302Z'
validated: true
submitted: true
---
# egrep

**Status**: Unverified

## Overview

egrep is an extended grep utility for searching patterns in text, used here to parse HTML responses for injected payloads.

## Description

It supports regex patterns to extract specific snippets, like isolating XSS injection points from curl output in security audits.

## Features

- Feature 1: Extended regex support
- Feature 2: Output only matches with -o
- Feature 3: Case-insensitive searching

## Installation

### Requirements

- GNU grep package

### Install Commands

```bash
# On Ubuntu/Debian
apt install grep

# Pre-installed on most Unix systems
```

## Basic Usage

```bash
egrep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-o` | Output only matching parts |
| `-i` | Ignore case |
| `-v` | Invert match |

## Examples

### Example 1: Basic Usage

```bash
egrep -o '<test>' file.html
```

### Example 2: Advanced Usage

```bash
egrep -o ".{47}?<test>.*?>" response.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Rarely detected as it's a standard utility
- Look for piped commands in logs

## Related Procedures

- [[procedures/Test-HTML-Injection-in-Search-Functionality]]

## Related Tools

- [[tools/grep]]

## References

- Official documentation: https://www.gnu.org/software/grep/manual/
