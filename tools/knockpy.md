---
id: tool-uuid-001
url: 'https://github.com/guelfoweb/knock'
tags:
  - reconnaissance
  - subdomain-enumeration
  - dns
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.979Z'
validated: true
submitted: true
---
# knockpy

**Status**: Unverified

## Overview

Knockpy is a Python-based tool for enumerating subdomains using brute-force and permutation techniques, ideal for discovering hidden attack surfaces in reconnaissance phases of security testing.

## Description

Knockpy performs DNS brute-forcing by generating permutations from wordlists and querying public resolvers. It's lightweight and effective for identifying forgotten subdomains pointing to services like Heroku, AWS, or GitHub, which can lead to takeover vulnerabilities. Commonly used in bug bounty hunting and pentesting.

## Features

- Feature 1: Brute-force subdomain discovery with built-in wordlists
- Feature 2: Permutation generation for common prefixes/suffixes (e.g., www, api)
- Feature 3: DNS record type querying (A, CNAME, MX)

## Installation

### Requirements

- Python 3.6+
- pip

### Install Commands

```bash
pip install knockpy
```

## Basic Usage

```bash
tool-name --help
```

Knockpy's help:

```bash
knockpy -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-w, --wordlist` | Specify custom wordlist |
| `-o, --output` | Save results to file |

## Examples

### Example 1: Basic Usage

```bash
knockpy target.com
```

### Example 2: Advanced Usage

```bash
knockpy -w /path/to/wordlist.txt target.com -o results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- DNS query spikes from a single source to the target's resolvers
- High volume of NXDOMAIN responses in DNS logs
- Network traffic patterns matching brute-force DNS requests

## Related Procedures

- [[procedures/Subdomain-Enumeration-with-Knockpy]]

## Related Tools

- [[subfinder]]
- [[amass]]

## References

- Official GitHub: https://github.com/guelfoweb/knock
- Related resources: OWASP Testing Guide on Reconnaissance
