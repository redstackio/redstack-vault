---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567897
url: 'https://censys.io'
tags:
  - reconnaissance
  - certificates
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:32.677Z'
validated: true
submitted: true
---
# Censys

**Status**: Unverified

## Overview

Censys is an internet-wide search engine for discovering hosts, services, and certificates, commonly used in security testing for passive reconnaissance of exposed infrastructure.

## Description

Censys indexes global internet data from protocols like HTTPS, providing searchable insights into certificates, IPs, and services. In offensive operations, it's used to find misconfigurations like self-signed certs on production servers, as in identifying IRCCloud's nginx at 54.153.101.52.

## Features

- Feature 1: Certificate search by subject, issuer, or tags
- Feature 2: Host discovery via IP and port scanning data
- Feature 3: Exportable results for further analysis

## Installation

### Requirements

- Web browser
- Free or paid account for API access

### Install Commands

No installation; web-based at https://censys.io.

## Basic Usage

```bash
# Web interface: Search in Certificates or Hosts section
```

### Common Options

| Option | Description |
|--------|-------------|
| Search Query | e.g., "IRCCloud" in certificates |
| Filters | By IP, port, protocol |

## Examples

### Example 1: Basic Usage

Search "IRCCloud" in certificates to find associated IPs.

### Example 2: Advanced Usage

Filter for self-signed certs: Query + "self-signed: true".

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API query logs if monitored
- Unusual traffic to censys.io from security tools

## Related Procedures

- [[procedures/Search-for-IRCCloud-Related-Certificates-Using-Censys]]

## Related Tools

- [[Shodan]]
- [[ZoomEye]]

## References

- Official documentation: https://docs.censys.io
- Related resources: Certificate Transparency explorations
