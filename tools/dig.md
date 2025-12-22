---
id: tool-001
url: 'https://www.dnsstuff.com/dig-command'
tags:
  - dns
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.306Z'
validated: true
submitted: true
---
# dig

**Status**: Unverified

## Overview

Dig (Domain Information Groper) is a flexible command-line DNS lookup tool used for querying DNS records, tracing delegations, and debugging name resolution. In security testing, it's commonly used for reconnaissance to map domains, subdomains, and infrastructure like CDNs.

## Description

Dig sends DNS queries to specified servers and displays detailed responses, including headers, questions, and answers. It's part of the BIND suite and excels at revealing CNAME chains, NS records, and IP mappings, essential for identifying hidden backends in attacks like CDN bypasses.

## Features

- Feature 1: Supports multiple query types (A, CNAME, MX, etc.)
- Feature 2: Tracing (+trace) for full resolution path
- Feature 3: Short mode (+short) for concise output

## Installation

### Requirements

- Standard Unix-like system or Windows with BIND tools

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install dnsutils

# On macOS (via Homebrew)
brew install bind

# On Windows: Download from ISC BIND
```

## Basic Usage

```bash
dig example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| +short | Brief answer only |
| +trace | Show full delegation chain |
| @server | Query specific DNS server |

## Examples

### Example 1: Basic Usage

```bash
dig A example.com
```

### Example 2: Advanced Usage

```bash
dig +trace A example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] DNS

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing high-volume DNS queries from a single source
- Query patterns targeting internal or sensitive domains

## Related Procedures

- [[procedures/DNS-Lookup-to-Identify-Origin-IP-Behind-Akamai]]

## Related Tools

- [[nslookup]]
- [[host]]

## References

- Official documentation: https://linux.die.net/man/1/dig
