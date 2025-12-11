---
url: ''
tags:
  - patch
  - fix
type: tool
platforms:
  - Linux
description: Tool for applying diffs to modify source code and fix vulnerabilities
id: 664d6b81-418d-4770-940b-dec027c7e18e
created_at: '2025-12-11T03:47:47.813Z'
updated_at: '2025-12-11T03:47:47.813Z'
verified: false
validated: true
submitted: true
---
# patch

**Status**: Unverified

## Overview

The patch utility applies differences to source files, used here to fix mruby's codegen.c.

## Description

Modifies code to pop loop contexts, preventing invalid jumps.

## Features

- Diff application
- Source modification

## Installation

### Requirements

- None

### Install Commands

```bash
sudo apt install patch
```

## Basic Usage

```bash
patch < fix.diff
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p1` | Strip path |

## Examples

### Example 1: Basic Usage

```bash
patch codegen.c < fix.diff
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques



### Tactics



## Detection

Indicators and methods for detecting this tool's usage:

- Monitor source code changes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #mruby

## References

- patch man page
