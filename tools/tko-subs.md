---
url: null
tags:
  - takeover-check
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.745Z'
id: 5ad2243e-bd2a-49d7-ab67-fe13d6a630e9
validated: true
submitted: true
---
# tko-subs

**Status**: Unverified

## Overview

tko-subs is a tool for checking subdomains for takeover vulnerabilities against cloud providers.

## Description

It validates if subdomains point to unused or dead resources in AWS, Azure, etc., by resolving and checking service availability.

## Features

- Feature 1: Multi-provider support (Azure, AWS, etc.)
- Feature 2: Batch processing from lists
- Feature 3: Detailed vulnerability reports

## Installation

### Requirements

- Go

### Install Commands

```bash
go install github.com/trap-bytes/tko-subs@latest
```

## Basic Usage

```bash
tko-subs -l list.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Subdomain list |

## Examples

### Example 1: Basic Usage

```bash
tko-subs -l subdomains.txt
```

### Example 2: Advanced Usage

```bash
tko-subs -l subdomains.txt -providers azure
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Queries to dead endpoints
- Tool binary on recon systems

## Related Procedures

- [[procedures/Enumerate-and-Verify-Dead-Subdomains]]

## Related Tools

- [[tools/subfinder]]

## References

- GitHub: https://github.com/trap-bytes/tko-subs
