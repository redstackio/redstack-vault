---
url: 'https://man7.org/linux/man-pages/man1/host.1.html'
tags:
  - dns
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.536Z'
id: 844e0d17-b81b-4672-9e2a-1a48a0e0420f
validated: true
submitted: true
---
# host-DNS-Lookup

**Status**: Unverified

## Overview

'host' is a standard Unix command-line tool for performing DNS lookups, querying hostnames for IP addresses, CNAMEs, and other records. In security testing, it's used for reconnaissance to detect misconfigurations like dangling CNAMEs in subdomain takeover scenarios.

## Description

The host tool interacts with DNS servers to resolve names, supporting various query types (A, CNAME, MX, etc.). It's lightweight, pre-installed on most Unix systems, and ideal for quick checks during offensive operations without needing additional setup. Common in pentesting for identifying vulnerable subdomains pointing to unclaimed services.

## Features

- Feature 1: Basic hostname resolution to IPs
- Feature 2: Specific record type queries (e.g., -t CNAME)
- Feature 3: Verbose output for detailed DNS paths

## Installation

### Requirements

- Unix-like OS (Linux, macOS)

### Install Commands

```bash
# Typically pre-installed; on Debian/Ubuntu:
apt-get install dnsutils

# On macOS, included in system tools
```

## Basic Usage

```bash
host --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t <type>` | Query specific record type (e.g., CNAME) |
| `-v` | Verbose output |
| `-a` | All records

## Examples

### Example 1: Basic Usage

```bash
host engineering.udemy.com
```

> Resolves to CNAME and IPs.

### Example 2: Advanced Usage

```bash
host -t CNAME engineering.udemy.com
```

> Shows only the alias record.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing DNS queries from unusual IPs
- Command-line audit logs containing 'host' executions
- Correlate with reconnaissance patterns on target domains

## Related Procedures

- [[procedures/Discover-Subdomain-Takeover-Opportunity-via-DNS-Lookup]]

## Related Tools

- [[dig]]
- [[nslookup]]

## References

- Official man page: https://man7.org/linux/man-pages/man1/host.1.html
- DNS reconnaissance guides
