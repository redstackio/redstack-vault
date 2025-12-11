---
url: ''
tags:
  - recon
  - directory
type: tool
platforms:
  - Linux
description: Displays directory structures in a tree-like format.
id: 4e47da9b-52cd-418c-b2e3-9db440267f3d
created_at: '2025-12-11T03:47:39.852Z'
updated_at: '2025-12-11T03:47:39.852Z'
verified: false
validated: true
submitted: true
---
# tree

**Status**: Unverified

## Overview

Tree is a command-line tool for displaying directory structures in a tree-like format, useful for verifying repository setups in exploits.

## Description

Commonly used in security testing to illustrate file and directory hierarchies, such as in PoCs for file-based vulnerabilities.

## Features

- Tree-like directory visualization
- Customizable output (e.g., levels, patterns)

## Installation

### Requirements

- Linux system

### Install Commands

```bash
sudo apt install tree
```

## Basic Usage

```bash
tree --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-a` | All files |

## Examples

### Example 1: Basic Usage

```bash
tree
```

### Example 2: Advanced Usage

```bash
tree -L 2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for tree command execution in logs
- Unusual directory traversals

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #git

## References

- Man page: tree(1)
