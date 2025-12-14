---
id: tool-dns-scanner
url: 'https://github.com/fwaeytens/dnsrecon'
tags:
  - dns
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.194Z'
validated: true
submitted: true
---
# DNS-scanner

**Status**: Unverified

## Overview

Tool for enumerating DNS records and subdomains during recon.

## Description

Scans for DNS issues on targets like Zomato, complementing web testing.

## Features

- Zone transfer attempts
- Subdomain brute-force
- Record enumeration

## Installation

### Requirements

- Python

### Install Commands

```bash
git clone https://github.com/darkoperator/dnsrecon
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
| -d | Domain |
| -t | Type (brt for brute) |

## Examples

### Example 1: Basic Usage

```bash
dnsrecon -d zomato.com
```

### Example 2: Advanced Usage

```bash
dnsrecon -d zomato.com -t brt -D /path/to/wordlist.txt
```

## MITRE ATT&CK Mapping

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- DNS query logs
- Rate limiting on resolvers

## Related Procedures

- [[procedures/Web-Application-Testing-with-Burp-Suite-and-DNS-Scanner]]

## Related Tools

- [[tools/Aquatone]]

## References

- GitHub repo
