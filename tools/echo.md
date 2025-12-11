---
url: ''
tags:
  - file
  - shell
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Shell command to display text or create files
id: de334005-9d17-40b1-981a-75018fd908a3
created_at: '2025-12-11T06:10:15.383Z'
updated_at: '2025-12-11T06:10:15.383Z'
verified: false
validated: true
submitted: true
---
# echo

**Status**: Unverified

## Overview

echo is a built-in shell command used to output text, often for creating test files in security demos.

## Description

Simple tool for writing strings to stdout or files, useful in preparing payloads or test data for exploits.

## Features

- Feature 1: Text output
- Feature 2: File redirection
- Feature 3: Variable expansion

## Installation

### Requirements

- Built-in to bash/sh

### Install Commands

```bash
# No installation needed
```

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
echo "Content" > /tmp/test
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor file creations in /tmp
- Detection method 2: Shell history logging

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[printf]]
- [[cat]]

## References

- Official documentation: man echo
