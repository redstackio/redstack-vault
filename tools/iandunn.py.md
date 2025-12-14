---
id: tool-iandunn-py-001
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/DpuAwysPx1fH7xHkcJ72Nn3d
tags:
  - ssrf
  - poc
  - exploit
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.038Z'
validated: true
submitted: true
---
# iandunn.py

**Status**: Unverified

## Overview

iandunn.py is a custom Python Proof-of-Concept script designed to exploit SSRF in WordPress xmlrpc.php by sending repeated pingback requests, forcing the server to fetch an arbitrary URL provided as input.

## Description

This script targets the pingback.ping XML-RPC method, crafting payloads where the source URL is the attacker's tracking link. It handles multiple iterations with configurable delays to demonstrate amplification potential for DDoS or recon. Developed for a specific HackerOne report, it prints response details for verification. Requires Python 3 and is run via command line, making it ideal for targeted exploitation in WordPress pentesting.

## Features

- Feature 1: Automated XML-RPC pingback submission
- Feature 2: Configurable request intervals for traffic simulation
- Feature 3: Error handling with fault string output

## Installation

### Requirements

- Python 3
- Download script from attachment

### Install Commands

```bash
# Download and save as iandunn.py
wget 'https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/DpuAwysPx1fH7xHkcJ72Nn3d' -O iandunn.py
chmod +x iandunn.py
```

## Basic Usage

```bash
python iandunn.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| Target URL | xmlrpc.php endpoint |
| Source URL | Tracking URL for SSRF |
| Wait Time | Delay in seconds |

## Examples

### Example 1: Basic Usage

```bash
python iandunn.py https://target.com/wordpress/xmlrpc.php https://grabify.link/XXXXXX 5
```

### Example 2: Advanced Usage

Modify for loops or integrate with other tools:

```bash
python iandunn.py https://target.com/xmlrpc.php http://internal.metadata 1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- XML-RPC POST requests with suspicious source URLs
- Repeated pingback calls from single IP
- Script execution logs showing python iandunn.py

## Related Procedures


## Related Tools

- [[Related Tool 1|tools/Python]]
- [[Related Tool 2|tools/xmlrpc-client]]

## References

- HackerOne Report: https://hackerone.com/reports/1004847
- Attachment download for script
