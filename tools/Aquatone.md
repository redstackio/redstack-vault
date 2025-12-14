---
id: tool-aquatone
url: 'https://github.com/michenriksen/aquatone'
tags:
  - subdomain
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.191Z'
validated: true
submitted: true
---
# Aquatone

**Status**: Unverified

## Overview

Subdomain discovery and screenshotting tool for visual recon.

## Description

Enumerates hidden domains for Zomato, providing screenshots to confirm existence.

## Features

- Subdomain brute-force
- Port scanning
- Screenshot capture
- Reporting

## Installation

### Requirements

- Go, Chrome

### Install Commands

```bash
go get github.com/michenriksen/aquatone
```

## Basic Usage

```bash
aquatone --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --domain | Target domain |
| --ports | Ports to scan |

## Examples

### Example 1: Basic Usage

```bash
aquatone-discover --domain zomato.com
```

### Example 2: Advanced Usage

```bash
aquatone-takeover --domain zomato.com
```

## MITRE ATT&CK Mapping

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- High volume HTTP requests
- Screenshot-like user agents

## Related Procedures

- [[procedures/Subdomain-Enumeration-with-Aquatone]]

## Related Tools

- [[tools/Maltego]]

## References

- GitHub repo
