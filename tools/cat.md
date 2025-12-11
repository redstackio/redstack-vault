---
url: null
tags:
  - file-read
type: tool
platforms:
  - Linux
description: >-
  Command-line utility to concatenate and display file contents, used for
  verification in exploits.
id: 96b74f2b-9213-4992-995d-6bd92e8ffbbe
created_at: '2025-12-11T06:10:40.377Z'
updated_at: '2025-12-11T06:10:40.377Z'
verified: false
validated: true
submitted: true
---
# cat

**Status**: Unverified

## Overview

cat is a standard Unix utility for reading and displaying file contents, often used to verify the results of file writes or command executions in security testing.

## Description

Simple tool for outputting file data to stdout, useful in post-exploitation verification.

## Features

- File content display
- Concatenation

## Installation

### Requirements

- Standard on Unix-like systems

### Install Commands

N/A

## Basic Usage

```bash
cat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Number lines |

## Examples

### Example 1: Basic Usage

```bash
cat file.txt
```

### Example 2: Advanced Usage

```bash
cat /tmp/vakzz
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Use Alternate Authentication Material]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- File access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]

## References

- cat man page
