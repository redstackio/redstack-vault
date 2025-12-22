---
url: 'https://binaryedge.io'
tags:
  - scanning
  - recon
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.622Z'
id: 0a65752c-a818-4f23-b236-3ce4e2061578
validated: true
submitted: true
---
# BinaryEdge-Scanner

**Status**: Unverified

## Overview

BinaryEdge is an internet scanning and threat intelligence platform used for discovering exposed services, including Kubernetes APIs, by querying global scan data.

## Description

In offensive security, BinaryEdge aggregates worldwide scans to identify vulnerabilities like open ports and service banners. For Kubernetes, it detects exposed APIs on port 6443 via signature matching. Common in red teaming for initial recon without active scanning.

## Features

- Feature 1: Global IP scanning with historical data
- Feature 2: Query API for specific services (e.g., 'kubernetes port:6443')
- Feature 3: Export results in JSON/CSV for further analysis

## Installation

### Requirements

- Web browser or API client (curl)
- API key for programmatic access

### Install Commands

```bash
# No install; use web UI at https://binaryedge.io or API
pip install requests  # For Python API client
```

## Basic Usage

```bash
tool-name --help  # Web-based; no CLI
```

### Common Options

| Option | Description |
|--------|-------------|
| Query: 'port:6443 kubernetes' | Search for exposed K8s APIs |
| API Key | Authenticate requests |

## Examples

### Example 1: Basic Usage

```bash
curl "https://api.binaryedge.io/v2/query?query=port:6443%20kubernetes&key=API_KEY"
```

### Example 2: Advanced Usage

```bash
curl "https://api.binaryedge.io/v2/query?query=port:6443%20%22Snapchat%22&key=API_KEY" | jq '.events[] | .target.ip'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API requests to binaryedge.io from scanning IPs
- High-volume queries in logs

## Related Procedures

- [[procedures/Scan-for-Exposed-Kubernetes-APIs]]

## Related Tools

- [[Shodan]]
- [[Censys]]

## References

- Official documentation: https://docs.binaryedge.io
- Related resources: HackerOne reports on exposed services
