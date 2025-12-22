---
url: 'https://binaryedge.io'
tags:
  - scanning
  - reconnaissance
type: tool
platforms:
  - Web
description: >-
  Cybersecurity search engine for discovering internet-exposed devices and
  services
id: 0592e1f2-baa2-4fe3-b500-9ed736291f3a
created_at: '2025-12-11T06:10:10.588Z'
updated_at: '2025-12-11T06:10:10.588Z'
verified: false
validated: true
submitted: true
---
# BinaryEdge

**Status**: Unverified

## Overview

BinaryEdge is a platform that scans and indexes internet-connected devices, allowing users to search for exposed services like Kubernetes APIs for vulnerability assessment.

## Description

It provides API and web-based querying for global scans, useful in reconnaissance for identifying misconfigured public endpoints.

## Features

- Global device scanning
- API for programmatic queries
- Historical data access

## Installation

### Requirements

- API key from BinaryEdge account
- curl or HTTP client

### Install Commands

No installation needed; use via web or API.

## Basic Usage

```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/search?query=product:kubernetes"
```

### Common Options

| Option | Description |
|--------|-------------|
| `-H "X-Key"` | API key header |

## Examples

### Example 1: Basic Usage

```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/search?query=port:6443"
```

### Example 2: Advanced Usage

```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/search?query=product:kubernetes country:US"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual API queries in network logs
- Traffic to binaryedge.io domains

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Shodan]]
- [[Censys]]

## References

- https://docs.binaryedge.io
