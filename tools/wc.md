---
id: tool-009
url: 'https://www.gnu.org/software/coreutils/wc'
tags:
  - count
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.911Z'
validated: true
submitted: true
---
# wc

**Status**: Unverified

## Overview

wc counts lines, words, characters; used in scripts to tally unsafe function occurrences.

## Description

Pipes grep output to wc -l for counts in scanning.

## Features

- Feature 1: Line counting
- Feature 2: Word/byte counts

## Installation

### Requirements

- Coreutils

### Install Commands

```bash
# Pre-installed
```

## Basic Usage

```bash
wc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Lines |

## Examples

### Example 1: Basic Usage

```bash
wc -l file
```

### Example 2: Advanced Usage

```bash
grep pattern | wc -l
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unix Shell]] Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

- Minimal footprint

## Related Procedures

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]

## Related Tools

- [[tools/awk]]

## References

- Coreutils manual
