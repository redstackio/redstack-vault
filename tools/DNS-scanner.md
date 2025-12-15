---
id: tool-dns-scanner-927413
url: null
tags:
  - dns
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.585Z'
validated: true
submitted: true
---
# DNS-Scanner

**Status**: Unverified

## Overview

Generic DNS enumeration tool for discovering subdomains, used alongside Burp for Zomato.

## Description

Tools like dnsenum or fierce for DNS recon to find hidden domains.

## Features

- Feature 1: Zone transfer attempts
- Feature 2: Brute-force subdomains
- Feature 3: Record enumeration

## Installation

### Requirements

- Perl/Python

### Install Commands

```bash
apt install dnsenum
```

## Basic Usage

```bash
dnsenum --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--enum` | Enumerate |
| `-f` | Wordlist |

## Examples

### Example 1: Basic Usage

```bash
dnsenum zomato.com
```

### Example 2: Advanced Usage

```bash
dnsenum -f /path/to/wordlist.txt zomato.com
```

## MITRE ATT&CK Mapping

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

- Excessive DNS queries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: subfinder]]

## References

- Tool-specific docs
