---
url: null
tags:
  - utility
  - formatting
type: tool
platforms:
  - Linux
  - macOS
description: >-
  Command-line utility for formatting and printing strings, used to craft HTTP
  requests with escape sequences.
id: 192cbae7-64f0-4470-8213-77f0a6efe783
created_at: '2025-12-13T09:01:17.647Z'
updated_at: '2025-12-13T09:01:17.647Z'
verified: false
validated: true
submitted: true
---
# printf

**Status**: Unverified

## Overview

printf is a shell command for outputting formatted strings, ideal for creating crafted payloads with CR and LF escapes in HTTP requests.

## Description

In security testing, it's used to build malformed requests for exploits like header smuggling.

## Features

- String formatting with escapes
- Output piping

## Installation

### Requirements

- Standard on Unix-like systems

### Install Commands

```bash
# Built-in
```

## Basic Usage

```bash
printf --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show help |

## Examples

### Example 1: Basic Usage

```bash
printf "formatted string\n"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor shell commands for unusual printf usage

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/nc]]

## References

- Man page for printf
