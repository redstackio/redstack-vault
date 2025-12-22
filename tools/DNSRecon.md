---
id: tool-001
url: 'https://github.com/darkoperator/dnsrecon'
tags:
  - recon
  - dns
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.192Z'
validated: true
submitted: true
---
# dnsrecon

**Status**: Unverified

**Status**: Unverified

## Overview

Dnsrecon is a DNS enumeration tool for security testing, used to discover subdomains, perform zone transfers, and identify misconfigurations like dangling records.

## Description

It supports brute-force, reverse lookups, and service discovery, ideal for finding takeover candidates in cloud environments like AWS.

## Features

- Feature 1: Subdomain brute-forcing with custom wordlists
- Feature 2: DNS record enumeration (A, CNAME, MX, etc.)
- Feature 3: Output in multiple formats (JSON, XML)

## Installation

### Requirements

- Python 3
- Kali Linux or similar

### Install Commands

```bash
git clone https://github.com/darkoperator/dnsrecon.git
cd dnsrecon
pip install -r requirements.txt
```

## Basic Usage

```bash
dnsrecon --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Target domain |
| `-t` | Test type (brt for brute) |
| `-D` | Dictionary file |

## Examples

### Example 1: Basic Usage

```bash
dnsrecon -d 8x8.com -t brt
```

### Example 2: Advanced Usage

```bash
dnsrecon -d 8x8.com -t brt -D /usr/share/wordlists/subdomains.txt -j output.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software]] Gather Victim Host Information: DNS

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual DNS query volumes from a single IP
- Brute-force patterns in DNS logs

## Related Procedures

- [[procedures/Discover-Dangling-DNS-Records]]

## Related Tools

- [[tools/subfinder]]
- [[tools/amass]]

## References

- Official GitHub repository
