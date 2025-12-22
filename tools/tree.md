---
url: ''
tags:
  - recon
type: tool
platforms:
  - Linux
description: Utility to display directory structures in a tree-like format.
id: 56c9fc4c-115e-4a95-889a-527ef2ea773c
created_at: '2025-12-11T06:10:22.593Z'
updated_at: '2025-12-11T06:10:22.593Z'
verified: false
validated: true
submitted: true
---
# tree

**Status**: Unverified

## Overview

Tree is a command-line tool used to recursively list directories in a tree-like format, helpful for visualizing file structures in exploits.

## Description

Commonly used in security testing to illustrate malicious directory setups, such as in command injection attacks.

## Features

- Tree-like directory display
- Level limiting
- File type indicators

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
| `-L` | Max display depth |

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

- Command execution logs
- Unusual directory listings

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[ls]]

## References

- Man page: tree(1)
