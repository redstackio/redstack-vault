---
url: ''
tags:
  - patching
type: tool
platforms:
  - macOS
description: Tool for generating file differences and patches
id: 3e8f0c92-3129-488e-9d88-5440d85774df
created_at: '2025-12-11T03:47:47.967Z'
updated_at: '2025-12-11T03:47:47.967Z'
verified: false
validated: true
submitted: true
---
# diff

**Status**: Unverified

## Overview

diff generates differences between files, used for creating patches in source code.

## Description

Essential for version control and applying fixes to vulnerabilities.

## Features

- File comparison
- Patch generation

## Installation

### Requirements

- Standard on Unix-like systems

### Install Commands

```bash
# Built-in
```

## Basic Usage

```bash
diff --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--git` | Git format |

## Examples

### Example 1: Basic Usage

```bash
diff file1 file2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques



### Tactics



## Detection

Indicators and methods for detecting this tool's usage:

- Command execution logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Git]]

## References

- man diff
