---
id: tool-006
url: 'https://www.gnu.org/software/sed/'
tags:
  - editor
  - extract
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.927Z'
validated: true
submitted: true
---
# sed

**Status**: Unverified

## Overview

Sed is a stream editor for filtering and transforming text, used to extract code lines.

## Description

Processes input line-by-line; here, -n 'range p' prints specific lines for review.

## Features

- Feature 1: Line range printing
- Feature 2: Substitution
- Feature 3: In-place editing

## Installation

### Requirements

- Unix-like

### Install Commands

```bash
# Pre-installed
```

## Basic Usage

```bash
sed --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | No auto-print |
| `p` | Print |

## Examples

### Example 1: Basic Usage

```bash
sed -n '10,15p' file
```

### Example 2: Advanced Usage

```bash
sed 's/old/new/g' file
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unix Shell]] Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

- Process monitoring

## Related Procedures

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]

## Related Tools

- [[tools/awk]]

## References

- Sed manual
