---
id: tool-h1-py3-script-001
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/112/671/.../h1-py3.py
tags:
  - custom-script
  - hackerone
  - monitoring
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.036Z'
validated: true
submitted: true
---
# h1-py3-script

**Status**: Unverified

## Overview

h1-py3.py is a custom Python 3 script for Linux to locate the last HackerOne report ID and poll for new submissions, exploiting response inconsistencies for real-time monitoring.

## Description

Similar to the py2 version but adapted for Python 3 syntax (e.g., input() instead of raw_input()), it automates ID scanning and logging, serving as a Linux-compatible PoC for the information disclosure.

## Features

- Feature 1: Compatible with Python 3 input handling
- Feature 2: Sequential polling with sleeps
- Feature 3: Datetime stamping for logs

## Installation

### Requirements

- Python 3.x on Linux
- requests library

### Install Commands

```bash
pip3 install requests
# Download script
wget <URL> -O h1-py3.py
```

## Basic Usage

```bash
python3 h1-py3.py
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Runs interactive monitoring |

## Examples

### Example 1: Basic Usage

```bash
python3 h1-py3.py
# Enter starting ID, begins polling
```

### Example 2: Advanced Usage

Execute with nohup for persistent monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Sequential API calls from Linux environments
- Python 3 request signatures

## Related Procedures

- [[procedures/Poll-for-New-Report-Submissions]]

## Related Tools

- [[tools/h1-py2-script]]
- [[tools/python-requests]]

## References

- HackerOne report attachment
