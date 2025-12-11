---
url: ''
tags:
  - file-creation
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Command-line utility to display text or create files
id: 90f67bd7-92ba-45df-8ab7-54488ca5223c
created_at: '2025-12-11T03:47:39.393Z'
updated_at: '2025-12-11T03:47:39.393Z'
verified: false
validated: true
submitted: true
---
# echo

**Status**: Unverified

## Overview

echo is a built-in shell command used to output text, often for creating test files in exploit setups.

## Description

Simple tool for writing content to stdout or files via redirection, useful in preparing payloads for security tests.

## Features
- Text output
- Variable expansion
- Redirection support

## Installation

### Requirements
- Built-in to bash/zsh

### Install Commands

N/A (built-in)

## Basic Usage

```bash
echo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | No trailing newline |
| `-e` | Enable backslash escapes |

## Examples

### Example 1: Basic Usage

```bash
echo hello > file.txt
```

### Example 2: Advanced Usage

```bash
echo -e "line1\nline2" > multi.txt
```

## MITRE ATT&CK Mapping

### Techniques
- [[Data from Local System]]

### Tactics
- [[Collection]]

## Detection

- File creation monitoring
- Command logging

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools
- #printf
- #cat

## References
- man echo
