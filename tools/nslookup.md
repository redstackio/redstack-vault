---
id: 123e4567-e89b-12d3-a456-426614174007
name: nslookup
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.854Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - dns
  - recon
url: 'https://man7.org/linux/man-pages/man1/nslookup.1.html'
validated: true
submitted: true
---

# nslookup

**Status**: Unverified

## Overview

nslookup is a command-line tool for querying DNS servers to obtain domain name or IP address mappings, commonly used in security testing for reconnaissance, such as identifying subdomain takeovers via CNAME checks.

## Description

Built into most OSes, nslookup allows interactive or one-shot queries for records like A, CNAME, MX. In offensive security, it's used to probe for misconfigurations like dangling DNS entries pointing to claimable cloud services. Features include server specification, query type filtering, and timeout options.

## Features

- Feature 1: Query specific record types (e.g., CNAME for takeovers)
- Feature 2: Use custom DNS resolvers to bypass caching
- Feature 3: Interactive mode for multiple queries

## Installation

### Requirements

- Standard on Unix-like systems; available via package managers on others

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt install dnsutils

# On Windows: Built-in

# On macOS: Built-in
```

## Basic Usage

```bash
nslookup --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -type= | Specify query type (e.g., CNAME) |
| server= | Use specific DNS server |
| -debug | Enable debug output |

## Examples

### Example 1: Basic Usage

```bash
nslookup saostatic.uber.com
```

### Example 2: Advanced Usage

```bash
nslookup saostatic.uber.com 8.8.8.8 -type=CNAME
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing DNS queries to public resolvers from unusual sources
- High volume of nslookup processes in endpoint logs

## Related Procedures

- [[procedures/Perform-DNS-Lookup-for-Subdomain-Takeover-Discovery]]

## Related Tools

- [[tools/dig]]
- [[tools/host]]

## References

- Official documentation: https://man7.org/linux/man-pages/man1/nslookup.1.html
- Related resources: DNS reconnaissance guides
