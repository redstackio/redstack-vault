---
url: ''
tags:
  - shell
type: tool
platforms:
  - Linux
description: Shell command to change directories.
id: f1889028-ac1a-4503-833e-1ac283dd1143
created_at: '2025-12-13T09:01:22.318Z'
updated_at: '2025-12-13T09:01:22.318Z'
verified: false
validated: true
submitted: true
---
# CD

**Status**: Unverified

## Overview

CD is a built-in shell command used to navigate file systems during setup and execution of attacks.

## Description

Essential for changing working directories in terminal-based workflows.

## Features

- Directory navigation

## Installation

### Requirements

- Bash shell

### Install Commands

Built-in, no installation needed.

## Basic Usage

```bash
cd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | N/A |

## Examples

### Example 1: Basic Usage

```bash
cd directory
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor shell history

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/git]]

## References

- Bash documentation
