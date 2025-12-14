---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
url: 'https://github.com/m4ll0k/takeover'
tags:
  - takeover
  - vulnerability
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.632Z'
validated: true
submitted: true
---
# Takeover

**Status**: Unverified

## Overview

Takeover is a tool for detecting subdomain takeover vulnerabilities by fingerprinting DNS records against common cloud services.

## Description

It checks if subdomains point to unused resources on platforms like AWS, Azure, or GitHub, allowing identification of claimable assets for exploitation in scenarios like the IBM 'vex.weather.com' vulnerability.

## Features

- Feature 1: Fingerprinting for 50+ services
- Feature 2: Batch processing of subdomain lists
- Feature 3: Customizable output and threading

## Installation

### Requirements

- Python 3.6+
- Pip for dependencies

### Install Commands

```bash
pip install takeover
```

## Basic Usage

```bash
takeover --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Input subdomain list |
| `--output` | Results file |
| `--threads` | Concurrency level |

## Examples

### Example 1: Basic Usage

```bash
takeover -l subs.txt
```

### Example 2: Advanced Usage

```bash
takeover -l subs.txt --threads 20 --output vulns.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- HTTP requests to service endpoints for fingerprinting
- Log entries for subdomain scans

## Related Procedures

- [[procedures/Detect-and-Exploit-Subdomain-Takeover]]

## Related Tools

- [[Subjack]]
- [[Dangerexpose]]

## References

- Official GitHub repository
