---
id: tool-uuid-001
url: 'https://github.com/melbadry9/SSLEnum'
name: SSLEnum
tags:
  - ssl
  - recon
  - subdomain-takeover
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.181Z'
validated: true
submitted: true
---
# SSLEnum

**Status**: Unverified

## Overview

SSLEnum is a Go-based tool for enumerating SSL/TLS certificate information from domains, detecting dangling or hijacked subdomains by analyzing certificate subjects, alternative names, and validity.

## Description

Designed for offensive security, SSLEnum retrieves certificate chains over HTTPS, parses fields like CN and SANs, and flags mismatches indicating subdomain takeovers. It's particularly useful in cloud environments where misconfigurations lead to certificate reuse across unrelated domains.

## Features

- Feature 1: Parses CN, SANs, issuer, and validity dates
- Feature 2: Detects dangling status via domain mismatches
- Feature 3: Supports batch enumeration for multiple subdomains

## Installation

### Requirements

- Go 1.16+
- Git

### Install Commands

```bash
git clone https://github.com/melbadry9/SSLEnum.git
cd SSLEnum
```

## Basic Usage

```bash
go run main.go -d max1.liveplan.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d, --domain` | Target domain |
| `-o, --output` | Save results to file |
| `-v, --verbose` | Detailed output |

## Examples

### Example 1: Basic Usage

```bash
go run main.go -d max1.liveplan.com
```

### Example 2: Advanced Usage

```bash
go run main.go -d max1.liveplan.com -o results.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to HTTPS endpoints with certificate parsing patterns
- Anomalous Go binary executions in logs

## Related Procedures

- [[procedures/Enumerate-SSL-Certificates-to-Confirm-Subdomain-Takeover]]

## Related Tools

- [[crt.sh]]
- [[Censys]]

## References

- Official GitHub: https://github.com/melbadry9/SSLEnum
- Certificate Transparency Logs
