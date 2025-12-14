---
url: 'https://thesprawl.org/projects/dnschef/'
tags:
  - dns
  - rebinding
  - ssrf
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.329Z'
id: bfa0f334-72fe-4e74-a21b-048bc8097b70
validated: true
submitted: true
---
# dnschef

**Status**: Unverified

## Overview

Dnschef is a DNS proxy tool designed for performing DNS rebinding attacks, commonly used in security testing to bypass IP blacklists by dynamically altering DNS resolutions during a single request.

## Description

In offensive security, dnschef acts as a man-in-the-middle for DNS queries, allowing attackers to serve different IP addresses for repeated lookups from the target server. A patched version handles mid-request changes, crucial for SSRF bypasses where initial resolutions pass validation but subsequent ones target internals like 169.254.169.254.

## Features

- Feature 1: Dynamic DNS record manipulation for rebinding
- Feature 2: Proxy mode for intercepting and forging responses
- Feature 3: Support for custom domains and TTL adjustments

## Installation

### Requirements

- Python 2.7 or 3.x
- Network privileges for port 53

### Install Commands

```bash
# Clone and run
pip install dnschef
# Or from source
git clone https://github.com/iphelix/dnschef.git
cd dnschef
python dnschef.py
```

## Basic Usage

```bash
dnschef.py -r --fakeip 127.0.0.1
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r, --rebind` | Enable rebinding mode |
| `--fakeip` | IP to return on second query |
| `-q, --quiet` | Suppress output |

## Examples

### Example 1: Basic Rebinding

```bash
dnschef.py -r --domain target.com --fakeip 169.254.169.254
```

### Example 2: Advanced Usage with Patch

```bash
dnschef.py --patched -r --listen 0.0.0.0:53 --fakeip 169.254.169.254
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous DNS queries with short TTLs or multiple resolutions
- Traffic to non-standard DNS ports or unexpected proxies
- Log analysis for rebinding patterns in server DNS caches

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://thesprawl.org/projects/dnschef/
- Related resources: DNS Rebinding Attacks on OWASP
