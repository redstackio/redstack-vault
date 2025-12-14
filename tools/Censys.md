---
url: 'https://censys.io'
tags:
  - recon
  - certificates
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.717Z'
id: 9a1f6754-f638-4c91-8ddf-7b5d2a888d5f
validated: true
submitted: true
---
# Censys

**Status**: Unverified

## Overview

Censys is a search engine for internet-connected devices and certificates, used in security testing for passive reconnaissance of domains, IPs, and ownership via SSL/TLS data.

## Description

Censys indexes global internet scan data, allowing queries for certificates to confirm domain ownership, such as linking fastly.sc-cdn.net to Snapchat. It's ideal for non-intrusive recon in subdomain takeover scenarios.

## Features

- Feature 1: Certificate and host searching
- Feature 2: Historical data access
- Feature 3: API for automated queries

## Installation

### Requirements

- Web browser or API key

### Install Commands

No installation; web-based.

## Basic Usage

```bash
# Web: Visit https://censys.io and search
```

### Common Options

| Option | Description |
|--------|-------------|
| Search Query | e.g., 'fastly.sc-cdn.net' |
| Filters | Certificate subjects, dates |

## Examples

### Example 1: Basic Usage

Search: https://censys.io/certificates?q=fastly.sc-cdn.net

### Example 2: Advanced Usage

API: curl 'https://search.censys.io/api/v2/certificates/search?q=parsed.names:fastly.sc-cdn.net' -H 'Authorization: Basic [API_KEY]'

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API key usage in logs
- Query patterns in network traffic

## Related Procedures

- [[procedures/Confirm-Domain-Ownership-with-Censys]]

## Related Tools

- [[Shodan]]
- [[crt.sh]]

## References

- Official documentation: https://docs.censys.io
- Related resources: Certificate Transparency Logs
