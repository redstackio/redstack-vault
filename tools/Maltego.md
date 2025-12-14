---
id: tool-maltego
url: 'https://www.maltego.com'
tags:
  - osint
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.187Z'
validated: true
submitted: true
---
# Maltego

**Status**: Unverified

## Overview

OSINT and link analysis tool for graphing relationships and recon.

## Description

Compares subdomain results from Aquatone, providing deeper entity links for Zomato recon.

## Features

- Entity transforms
- Graph visualization
- Data mining
- Export options

## Installation

### Requirements

- Java

### Install Commands

```bash
# Download from site
wget https://www.maltego.com/downloads/maltego_desktop_linux.sh
chmod +x maltego_desktop_linux.sh
./maltego_desktop_linux.sh
```

## Basic Usage

```bash
# GUI, launch maltego
```

### Common Options

| Option | Description |
|--------|-------------|
| Transforms | Run entity expansions |

## Examples

### Example 1: Basic Usage

Create graph, add Domain entity, run To Subdomain transform.

### Example 2: Advanced Usage

Import CSV of subdomains, apply DNS transforms.

## MITRE ATT&CK Mapping

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Services

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- API query patterns to transforms
- Unusual graph queries

## Related Procedures

- [[procedures/Subdomain-Comparison-with-Maltego]]

## Related Tools

- [[tools/Aquatone]]

## References

- Official site
