---
url: 'https://www.shodan.io/'
tags:
  - recon
  - scanning
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.904Z'
id: 51e69948-9880-4ada-89f6-855b255eed0a
validated: true
submitted: true
---
# Shodan

**Status**: Unverified

## Overview

Shodan is a search engine for internet-connected devices, used in security testing to discover exposed services like unauthenticated Docker Registries.

## Description

Shodan indexes banners from devices and services, allowing queries with dorks to find vulnerabilities. In offensive ops, it's used for reconnaissance to identify public-facing apps without auth.

## Features

- Feature 1: Advanced search dorks for products, countries, certs
- Feature 2: API integration for automated scans
- Feature 3: Historical data and exploit integration

## Installation

### Requirements

- Python 3
- API key from shodan.io

### Install Commands

```bash
pip install shodan
shodan init YOUR_API_KEY
```

## Basic Usage

```bash
shodan search 'docker'
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --fields | Limit output fields |

## Examples

### Example 1: Basic Usage

```bash
shodan search 'port:443 docker'
```

### Example 2: Advanced Usage

```bash
shodan search 'ssl.cert.subject.cn:*.mil product:"Docker Registry"' --fields ip_str
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API key usage logs on Shodan
- Unusual query patterns in network traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: Nmap]]
- [[Related Tool: Masscan]]

## References

- Official documentation: https://developer.shodan.io/
