---
url: null
tags:
  - poc
  - privilege-escalation
type: tool
platforms:
  - Windows
description: Proof-of-concept script for local privilege escalation via EvoStream API
id: abbaef9c-3209-4f0d-a479-f50b196935ad
created_at: '2025-12-11T06:10:22.810Z'
updated_at: '2025-12-11T06:10:22.810Z'
verified: false
validated: true
submitted: true
---
# poc.py

**Status**: Unverified

## Overview

Python script demonstrating local exploitation of the EvoStream API for privilege escalation.

## Description

Uses WebSocket to send 'launchprocess' commands, running arbitrary binaries as SYSTEM.

## Features

- WebSocket connection handling
- Command injection payload
- Privilege escalation demo

## Installation

### Requirements

- Python 3
- websocket-client library

### Install Commands

```bash
pip install websocket-client
```

## Basic Usage

```bash
python poc.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

```bash
python poc.py --command 'whoami'
```

### Example 2: Advanced Usage

```bash
python poc.py --binary 'calc.exe'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor WebSocket traffic to localhost:7440
- Detect unexpected SYSTEM processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rce0923234.html]]

## References

- HackerOne report #544928
