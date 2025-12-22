---
id: tool-hackeronebrute
url: null
tags:
  - brute-force
  - custom-script
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.759Z'
validated: true
submitted: true
---
# hackeronebrute.py

**Status**: Unverified

## Overview

Custom Python script for brute-forcing web login credentials by rotating IPv6 addresses to bypass IP rate limiting.

## Description

Designed for the HackerOne endpoint, it uses multithreading (e.g., 50 threads) to cycle through IPv6 addresses on a specified interface, sending POST requests with username and sequential passwords from a file. Ensures 4-second spacing per IP to evade blocks.

## Features

- Feature 1: IPv6 address rotation from /64 subnet
- Feature 2: Multithreaded requests (~30 pw/s)
- Feature 3: Progress tracking and success notification

## Installation

### Requirements

- Python 2/3
- requests library: pip install requests

### Install Commands

```bash
# Download or create script
wget custom-script.py -O hackeronebrute.py
pip install requests
```

## Basic Usage

```bash
python hackeronebrute.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --debug | Enable debug output |

## Examples

### Example 1: Basic Usage

```bash
python hackeronebrute.py username passwords.txt interface 50
```

### Example 2: Advanced Usage

```bash
python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50 --debug
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Connection Proxy]] Proxy

### Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of login attempts from sequential IPv6 addresses
- Scripted POST patterns to /sessions
- Traffic from VPS IPs

## Related Procedures

- [[procedures/Execute-Brute-Force-Script]]

## Related Tools

- [[tools/Python]]

## References

- Custom script based on HackerOne report
