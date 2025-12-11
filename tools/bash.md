---
url: null
tags:
  - shell
  - execution
type: tool
platforms:
  - Linux
description: Unix shell and command language
id: 531245e4-8198-4063-b3cb-00eec1dfcc21
created_at: '2025-12-11T06:10:31.257Z'
updated_at: '2025-12-11T06:10:31.257Z'
verified: false
validated: true
submitted: true
---
# bash

**Status**: Unverified

## Overview

Bash is a Unix shell used for executing commands, here in reverse shell payloads.

## Description

Alternative payload uses bash to create interactive reverse shells.

## Features

- Command execution
- Scripting

## Installation

Pre-installed on most Linux systems.

## Basic Usage

```bash
bash -i
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c` | Execute command |
| `-i` | Interactive |

## Examples

### Example 1: Basic Usage

```bash
bash -c 'command'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

- Monitor bash processes
- Unusual network connections

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/python]]

## References

- https://www.gnu.org/software/bash/
