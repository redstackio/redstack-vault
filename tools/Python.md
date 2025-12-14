---
id: tool-uuid-003
url: 'https://www.python.org/'
tags:
  - programming-language
  - scripting
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.492Z'
validated: true
submitted: true
---
# Python

**Status**: Unverified

## Overview

Python is a versatile programming language used for scripting and running web frameworks like Flask in security PoCs.

## Description

Serves as the runtime for the Flask server in this SSRF test, enabling quick setup of test environments.

## Features

- Feature 1: Extensive standard library
- Feature 2: Easy scripting for automation
- Feature 3: Cross-platform compatibility

## Installation

### Requirements

- OS package support

### Install Commands

```bash
# Linux
apt install python3

# macOS
brew install python

# Windows
# Download from python.org
```

## Basic Usage

```bash
python --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c` | Execute code from command line |
| `-m` | Run library module |

## Examples

### Example 1: Basic Usage

```bash
python -c "print('Hello')"
```

### Example 2: Advanced Usage

```bash
python server.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- python.exe processes
- Script executions in logs

## Related Procedures


## Related Tools

- [[tools/curl]]

## References

- Official documentation: https://docs.python.org/3/
