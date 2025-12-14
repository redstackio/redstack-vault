---
id: tool-010
url: 'https://www.gnu.org/software/coreutils/tee'
tags:
  - logging
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.908Z'
validated: true
submitted: true
---
# tee

**Status**: Unverified

## Overview

Tee duplicates output to file and stdout, used for logging Valgrind results.

## Description

Splits pipe output; 2>&1 | tee log captures stderr too.

## Features

- Feature 1: Dual output
- Feature 2: Append mode

## Installation

### Requirements

- Coreutils

### Install Commands

```bash
# Pre-installed
```

## Basic Usage

```bash
tee --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-a` | Append |

## Examples

### Example 1: Basic Usage

```bash
command | tee file.log
```

### Example 2: Advanced Usage

```bash
command 2>&1 | tee -a log
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unix Shell]] Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

- File creation timestamps

## Related Procedures

- [[procedures/Dynamic-Memory-Testing-of-cURL-with-Valgrind]]

## Related Tools

- [[tools/redirect]]

## References

- Coreutils manual
