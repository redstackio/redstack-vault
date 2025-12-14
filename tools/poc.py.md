---
id: tool-poc-py
url: null
tags:
  - poc
  - rce
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.502Z'
validated: true
submitted: true
---
# poc.py

**Status**: Unverified

## Overview

Proof-of-concept Python script for local exploitation of EvoStream API to execute commands as SYSTEM.

## Description

The script sends HTTP POST requests to localhost:7440/jsonrpc with launchprocess params, demonstrating privilege escalation by running binaries like calc.exe.

## Features

- JSON-RPC API interaction
- Arbitrary binary execution
- Local testing without authentication

## Installation

### Requirements

- Python 3.x
- requests library

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python poc.py
```

### Common Options

| Option | Description |
|--------|-------------|
| --binary | Path to executable |
| --args | Arguments string |

## Examples

### Example 1: Basic Usage

```bash
python poc.py --binary calc.exe
```

### Example 2: Advanced Usage

```bash
python poc.py --binary cmd.exe --args "/c whoami"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to localhost:7440 from Python
- Unexpected SYSTEM process spawns

## Related Procedures

- [[procedures/Local-Privilege-Escalation-via-LaunchProcess-Command]]

## Related Tools

- [[tools/rce0923234.html]]

## References

- HackerOne Report #544928
