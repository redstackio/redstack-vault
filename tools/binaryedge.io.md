---
url: 'https://binaryedge.io'
tags:
  - scanning
  - reconnaissance
type: tool
platforms:
  - Web
description: >-
  A platform for global internet scanning and asset discovery, used to identify
  exposed services like Kubernetes APIs.
id: 6a16bbc1-de96-4f87-9da9-9dbf9dee9aa8
created_at: '2025-12-10T05:44:16.321Z'
updated_at: '2025-12-10T05:44:16.321Z'
verified: false
validated: true
submitted: true
---
# binaryedge.io

**Status**: Unverified

## Overview

Binaryedge.io is a cybersecurity platform that provides global scanning capabilities to discover exposed internet assets, including services, ports, and vulnerabilities.

## Description

It aggregates data from worldwide scans, allowing users to query for specific technologies like Kubernetes APIs. Commonly used in offensive security for reconnaissance and identifying misconfigurations.

## Features

- Global asset discovery: Scan for IPs, ports, and services
- Historical data: Access past scan results
- API integration: Programmatic access for automation

## Installation

### Requirements

- Account registration on binaryedge.io
- API key for advanced usage

### Install Commands

```bash
# No installation needed; web-based platform
# For API: Use curl or Python requests
```

## Basic Usage

```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/ip/ target-ip"
```

### Common Options

| Option | Description |
|--------|-------------|
| `-H "X-Key"` | API authentication |
| `/query/search` | Search endpoint |

## Examples

### Example 1: Basic Usage

```bash
# Web interface: Search for "kubernetes port:6443"
```

### Example 2: Advanced Usage

```bash
curl -H "X-Key: KEY" "https://api.binaryedge.io/v2/query/search?query=product:kubernetes"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]
- [[Network Service Scanning]]

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for API requests to binaryedge.io domains
- Unusual outbound traffic patterns to scanning services

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Shodan]]
- [[tools/Censys]]

## References

- https://binaryedge.io/docs
- Related scanning resources
