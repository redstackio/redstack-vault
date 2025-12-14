---
url: 'https://man7.org/linux/man-pages/man1/nslookup.1.html'
tags:
  - dns
  - recon
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.439Z'
id: a671680d-644c-4855-8f4a-f3a2f26052c7
validated: true
submitted: true
---
# nslookup

**Status**: Unverified

## Overview

nslookup is a command-line tool for querying DNS servers to resolve hostnames, retrieve records like CNAME, A, and MX, commonly used in security testing for reconnaissance and identifying misconfigurations.

## Description

nslookup allows users to interact with DNS to obtain detailed resolution information, making it ideal for detecting subdomain takeovers by revealing dangling CNAMEs pointing to unused services. It's built into most operating systems and supports interactive and non-interactive modes for offensive security operations like mapping attack surfaces.

## Features

- Feature 1: Query specific record types (e.g., CNAME, A)
- Feature 2: Interactive mode for multiple queries
- Feature 3: Server specification for authoritative responses

## Installation

### Requirements

- Standard on Linux, Windows, macOS (no installation needed)

### Install Commands

```bash
# On Linux if missing: sudo apt install dnsutils
```

## Basic Usage

```bash
nslookup --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -type= | Specify record type (e.g., CNAME) |
| -server= | Use specific DNS server |

## Examples

### Example 1: Basic Usage

```bash
nslookup engineering.zomato.com
```

### Example 2: Advanced Usage

```bash
nslookup -type=CNAME engineering.zomato.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing DNS queries to unusual subdomains
- Command-line audit logs with nslookup executions

## Related Procedures

- [[procedures/Detect-Subdomain-Takeover-via-DNS-Lookup]]

## Related Tools

- [[dig]]
- [[host]]

## References

- Official documentation: https://man7.org/linux/man-pages/man1/nslookup.1.html
- Related resources: DNS reconnaissance guides
