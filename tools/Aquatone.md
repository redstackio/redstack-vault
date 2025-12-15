---
id: tool-aquatone-927413
url: 'https://github.com/michenriksen/aquatone'
tags:
  - subdomain
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.580Z'
validated: true
submitted: true
---
# Aquatone

**Status**: Unverified

## Overview

Aquatone enumerates subdomains and takes screenshots, revealing hidden Zomato domains.

## Description

Go-based tool for fast subdomain discovery and visual recon.

## Features

- Feature 1: Passive/active enum
- Feature 2: Screenshot automation
- Feature 3: Takeover detection

## Installation

### Requirements

- Go 1.8+

### Install Commands

```bash
go get github.com/michenriksen/aquatone
```

## Basic Usage

```bash
aquatone-discover --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--domain` | Target |
| `--threads` | Concurrency |

## Examples

### Example 1: Basic Usage

```bash
aquatone-discover --domain zomato.com
```

### Example 2: Advanced Usage

```bash
aquatone-discover --domain zomato.com --threads 50
```

## MITRE ATT&CK Mapping

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

- DNS query bursts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: Maltego]]

## References

- GitHub repo
