---
url: ''
tags:
  - python
  - pickle
  - rce
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.970Z'
id: 62a7fba6-8315-4951-a0fd-a87e857f5dd7
validated: true
submitted: true
---
# Custom-Python-Pickle-Script

**Status**: Unverified

## Overview

A custom Python script to generate base64-encoded malicious pickles exploiting unpickling for arbitrary code execution via __reduce__.

## Description

Uses cPickle to serialize a PickleRce object that reduces to os.system with a provided command, typically a reverse shell. Ideal for deserialization attacks on internal services.

## Features

- Feature 1: __reduce__ gadget for command execution
- Feature 2: Base64 encoding for param injection
- Feature 3: Default reverse shell template

## Installation

### Requirements

- Python 2.7 or 3.x with cPickle (or pickle)

### Install Commands

```bash
# Save as pickle_exploit.py and run with python
```

## Basic Usage

```bash
python pickle_exploit.py [command]
```

### Common Options

| Option | Description |
|--------|-------------|
| [command] | Custom os.system arg |

## Examples

### Example 1: Basic Usage

```bash
python pickle_exploit.py
```

### Example 2: Advanced Usage

```bash
python pickle_exploit.py "whoami > /tmp/pwned"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Command and Scripting Interpreter: Python

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Scan for pickle data in logs/params
- Monitor base64 decodes in Python services

## Related Procedures

- [[procedures/Exploit-Python-Unpickling-in-Internal-Service]]

## Related Tools

- [[Custom PHP Exploit Script]]

## References

- Python pickle security docs
