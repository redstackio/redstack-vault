---
id: tool-host
url: 'https://linux.die.net/man/1/host'
tags:
  - dns
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows (with BIND tools)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.147Z'
validated: true
submitted: true
---
# host

**Status**: Unverified

## Overview

'host' is a standard command-line DNS lookup utility for querying domain resolution, including A records, CNAME aliases, and MX records. It is commonly used in security testing for reconnaissance, verifying subdomain configurations, and identifying takeover vulnerabilities through dangling records.

## Description

The host tool sends DNS queries to resolve names and retrieve record details, supporting options for specific record types and verbose output. In offensive security, it helps trace misconfigurations like unused CNAMEs pointing to claimable services (e.g., AWS S3, WordPress.com). It is lightweight, built into most Unix-like systems, and ideal for quick checks without additional setup.

## Features

- Feature 1: Basic DNS resolution for IPs and aliases
- Feature 2: Support for querying specific record types (A, CNAME, NS)
- Feature 3: Short and long output formats for concise or detailed results

## Installation

### Requirements

- Standard on Linux/macOS; for Windows, install BIND tools or use Cygwin

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install dnsutils

# On macOS (if missing)
brew install bind
```

## Basic Usage

```bash
host --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output |
| -t type | Query specific record type (e.g., CNAME) |

## Examples

### Example 1: Basic Usage

```bash
host code.wordpress.net
```

### Example 2: Advanced Usage

```bash
host -t CNAME code.wordpress.net
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing DNS queries from unusual IPs
- Command-line audit logs with 'host' executions
- Monitor for repeated queries to target domains

## Related Procedures

- [[procedures/Detect-and-Confirm-Subdomain-Takeover]]

## Related Tools

- [[dig]]
- [[nslookup]]

## References

- Official documentation: https://linux.die.net/man/1/host
- Related resources: DNS reconnaissance guides in OWASP testing methodology
