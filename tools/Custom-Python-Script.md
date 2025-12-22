---
url: null
tags:
  - python
  - deserialization
type: tool
platforms:
  - Linux
description: Custom script for generating malicious Python pickle objects for RCE.
id: f52a44f2-e451-4be9-9d21-c80e2bc4a4e1
created_at: '2025-12-13T09:00:27.996Z'
updated_at: '2025-12-13T09:00:27.996Z'
verified: false
validated: true
submitted: true
---
# Custom Python Script

**Status**: Unverified

## Overview

A custom Python script to craft base64-encoded pickle objects that execute arbitrary commands upon deserialization, used for RCE exploits.

## Description

The script defaults to generating a pickle that runs a reverse shell but can take custom commands. It's used to exploit insecure deserialization in Python services.

## Features

- Generates malicious pickle payloads
- Supports custom command injection
- Base64 encoding for transmission

## Installation

### Requirements

- Python installed

### Install Commands

```bash
# No installation needed; run directly
```

## Basic Usage

```bash
python pickle_exploit.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `command` | Optional command to execute |

## Examples

### Example 1: Basic Usage

```bash
python pickle_exploit.py
```

### Example 2: Advanced Usage

```bash
python pickle_exploit.py --command "ls -la"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for Python executions creating pickle files
- Detect base64 patterns in network traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Netcat]]

## References

- HackerOne report: https://hackerone.com/reports/415501
