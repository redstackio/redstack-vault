---
url: 'https://github.com/projectdiscovery/subfinder'
tags:
  - reconnaissance
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.925Z'
id: 1756278c-c9e2-45cc-a3d3-a9917ea515e5
validated: true
submitted: true
---
# subfinder

**Status**: Unverified

## Overview

Fast passive subdomain enumeration tool using OSINT sources.

## Description

Subfinder performs subdomain discovery without direct DNS queries, ideal for stealthy recon in attack chains.

## Features

- Feature 1: Multiple passive sources
- Feature 2: Silent mode
- Feature 3: Output to file

## Installation

### Requirements

- Go 1.16+

### Install Commands

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## Basic Usage

```bash
subfinder -d example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Domain |
| `-o` | Output |

## Examples

### Example 1: Basic Usage

```bash
subfinder -d bountypay.h1ctf.com -o subs.txt
```

### Example 2: Advanced Usage

```bash
subfinder -d target -all -o allsubs.txt
```

## MITRE ATT&CK Mapping

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- Network traffic to known OSINT APIs
- DNS query patterns

## Related Procedures

- [[procedures/Enumerate-Subdomains-and-Expose-Git-Repository]]

## Related Tools

- [[tools/amass]]

## References

- Official GitHub repo
