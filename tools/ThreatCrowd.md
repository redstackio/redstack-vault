---
id: tool-threatcrowd-001
url: 'https://www.threatcrowd.org/'
tags:
  - reverse-dns
  - recon
  - threat-intel
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.859Z'
validated: true
submitted: true
---
# ThreatCrowd

**Status**: Unverified

## Overview

ThreatCrowd is an online threat intelligence platform providing reverse DNS lookups, IP/domain reputation, and vulnerability scoping data, useful for identifying domains vulnerable to takeovers by querying shared infrastructure.

## Description

In security testing, ThreatCrowd helps enumerate the scope of vulnerabilities like subdomain takeovers by revealing domains resolving to specific IPs (e.g., Unbounce servers). Users query via web interface for reverse lookups on IPs to find dangling CNAMEs pointing to exploitable services.

## Features

- Feature 1: Reverse IP/DNS resolution
- Feature 2: Domain-IP associations
- Feature 3: Threat indicators and malware links

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

N/A (web-based)

## Basic Usage

```bash
# No CLI; access via browser
curl "https://www.threatcrowd.org/ip.php?ip=54.225.142.127"
```

### Common Options

| Option | Description |
|--------|-------------|
| ip= | IP address for reverse lookup |
| domain= | Domain for forward queries |

## Examples

### Example 1: Basic Usage

Query https://www.threatcrowd.org/ip.php?ip=54.225.142.127 for domains on Unbounce IP.

### Example 2: Advanced Usage

Use API for automated queries if available.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API query logs from ThreatCrowd IPs
- Increased reconnaissance traffic to intel sites

## Related Procedures

- [[procedures/Verify-Subdomain-Takeover]]

## Related Tools

- [[VirusTotal]]
- [[Shodan]]

## References

- Official documentation: https://www.threatcrowd.org/
- Related resources: Threat intelligence APIs
