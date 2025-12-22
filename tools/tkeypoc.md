---
url: 'https://github.com/elceef/tkeypoc/'
tags:
  - exploit
  - dos
  - python
type: tool
platforms:
  - Linux
description: Python PoC exploit for CVE-2015-5477 BIND9 TKEY DoS vulnerability.
id: fae5fff0-2d92-4d64-ab39-d4a9bc28ec93
created_at: '2025-12-14T17:26:36.869Z'
updated_at: '2025-12-14T17:26:36.869Z'
verified: false
validated: true
submitted: true
---
# tkeypoc

**Status**: Unverified

## Overview

tkeypoc is a simple Python proof-of-concept script that sends malformed TKEY DNS queries to exploit a denial of service vulnerability in BIND9, causing server crashes.

## Description

The tool constructs a specific UDP payload with invalid TKEY elements, triggering BIND9's handling flaw. It's designed for demonstration on vulnerable servers like those on port 53 of ci.nextcloud.com.

## Features

- Feature 1: Hardcoded malformed DNS payload
- Feature 2: UDP socket transmission
- Feature 3: Command-line target specification

## Installation

### Requirements

- Python 2/3
- No external dependencies

### Install Commands

```bash
# Clone from GitHub
git clone https://github.com/elceef/tkeypoc/
cd tkeypoc
chmod +x tkeypoc.py
```

## Basic Usage

```bash
python tkeypoc.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| Target (positional) | Host to attack |

## Examples

### Example 1: Basic Usage

```bash
python tkeypoc.py ci.nextcloud.com
```

### Example 2: Advanced Usage

Run directly with target IP.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- UDP packet captures showing malformed TKEY queries
- BIND9 logs with assertion failures

## Related Procedures

- [[procedures/Exploit-BIND9-TKEY-Vulnerability-with-PoC]]

## Related Tools

- [[Scapy]]

## References

- GitHub repo: https://github.com/elceef/tkeypoc/
