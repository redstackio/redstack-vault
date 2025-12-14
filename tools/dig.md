---
url: 'https://linux.die.net/man/1/dig'
tags:
  - dns
  - reconnaissance
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows (via Cygwin)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.344Z'
id: 2bfacb0a-df80-4862-aa14-f609259f4a4e
validated: true
submitted: true
---
# dig

**Status**: Unverified

## Overview

Dig (Domain Information Groper) is a flexible command-line tool for querying DNS nameservers, commonly used in security testing to enumerate domain records, identify misconfigurations like dangling CNAMEs, and map attack surfaces.

## Description

Dig sends DNS queries to specified servers and displays responses in a human-readable format. In offensive security, it's essential for reconnaissance, such as checking for subdomain takeovers by resolving CNAMEs to unclaimed PaaS/IaaS resources like AWS CloudFront.

## Features

- Feature 1: Supports multiple query types (A, CNAME, NS, MX)
- Feature 2: Customizable output with +short, +trace, +cmd flags
- Feature 3: Queries any DNS server, including root servers for authoritative info

## Installation

### Requirements

- Standard on most Unix-like systems
- For Windows: Install via BIND tools or Cygwin

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install dnsutils

# On macOS (via Homebrew)
brew install bind
```

## Basic Usage

```bash
dig --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `+short` | Abbreviated answers only |
| `+trace` | Trace full DNS path |
| `+cmd` | Include command in output |

## Examples

### Example 1: Basic Usage

```bash
dig cloudfront.ubnt.com
```

### Example 2: Advanced Usage

```bash
dig +short +cmd cloudfront.ubnt.com A
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Identify Business Systems

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing DNS queries to target domains from unusual IPs
- Process monitoring for dig.exe or dig binary execution
- SIEM alerts on high-volume DNS reconnaissance patterns

## Related Procedures

- [[procedures/Detect-Dangling-CNAME-with-DNS-Lookup]]

## Related Tools

- [[nslookup]]
- [[host]]

## References

- Official documentation: https://bind9.readthedocs.io/en/v9_16_21/utilities.html#dig
- Related resources: DNS reconnaissance guides on OWASP
