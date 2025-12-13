---
url: ''
tags:
  - shell
  - payload-generation
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Shell command to display text or variables.
id: c9dc30f1-df3c-4111-9584-c445bd3c4150
created_at: '2025-12-13T09:01:22.386Z'
updated_at: '2025-12-13T09:01:22.386Z'
verified: false
validated: true
submitted: true
---
# echo

**Status**: Unverified

## Overview

Echo is a built-in shell command used to output strings, often for generating payloads in scripts or one-liners.

## Description

In security contexts, echo is used to craft and output complex strings like HTTP payloads for piping to network tools.

## Features

- String output
- Escape sequence handling

## Installation

### Requirements

- Built-in to most shells

### Install Commands

```bash
# Built-in, no install needed
```

## Basic Usage

```bash
echo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Suppress trailing newline |

## Examples

### Example 1: Basic Usage

```bash
echo -n 'payload'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Script analysis for payload generation
- Command line logging

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/printf]]

## References

- man echo
