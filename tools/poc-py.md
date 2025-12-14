---
id: tool-poc-py
url: 'https://github.com/tintinweb/pub/tree/master/pocs/cve-2016-2563'
tags:
  - ssh
  - poc
  - exploit
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.688Z'
validated: true
submitted: true
---
# poc-py

**Status**: Unverified

## Overview

poc.py is a Python script that implements a malicious SSH server to demonstrate CVE-2016-2563 by sending crafted responses during file transfers and packet handling to exploit PuTTY clients.

## Description

The tool acts as an SSH server compatible with PuTTY, handling authentication and then delivering payloads for stack buffer overflow in file size parsing, null pointer reads in string handling, and channel requests. It's used in offensive security for client-side exploit PoCs, targeting Windows PuTTY <=0.66 over SSH on port 22. Features include automated payload crafting (e.g., 'A'*1000 for overflow) and logging of triggers.

## Features

- Feature 1: Simulates SSH server with post-auth exploit responses
- Feature 2: Triggers RCE via file size buffer overflow
- Feature 3: Includes DoS vectors for string parsing and TCP forwarding

## Installation

### Requirements

- Python 2.7 or 3.x
- paramiko library (pip install paramiko)

### Install Commands

```bash
# Clone repo
git clone https://github.com/tintinweb/pub.git
cd pub/pocs/cve-2016-2563
pip install paramiko
```

## Basic Usage

```bash
python poc.py
```

### Common Options

| Option | Description |
|--------|-------------|
| None (script-based) | Runs server on port 22; edit source for custom payloads |

## Examples

### Example 1: Basic Usage

```bash
python poc.py
```
Connect with PuTTY to trigger.

### Example 2: Advanced Usage

Modify poc.py to change overflow size, then run:

```bash
python poc.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[T1587.001]] Develop Capabilities: Malware

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Python SSH server on non-standard impl
- Unusual port 22 traffic with malformed packets
- PoC repo downloads in threat intel feeds

## Related Procedures

- [[procedures/Set-Up-Malicious-SSH-PoC-Server]]

## Related Tools

- [[Related Tool|tools/PuTTY-PSCP]]

## References

- HackerOne Report: https://hackerone.com/reports/120903
- CVE-2016-2563
