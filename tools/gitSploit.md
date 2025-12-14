---
id: tool-gitsploit
url: 'https://github.com/arthaudtz/gitsploit'
tags:
  - github-vuln
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.181Z'
validated: true
submitted: true
---
# gitSploit

**Status**: Unverified

## Overview

Framework to exploit GitHub for finding vulnerabilities in public code repos.

## Description

Scans Zomato repos for patterns like XSS, IDOR, revealing ~10 issues.

## Features

- GitHub API searches
- Vuln pattern matching
- Report generation

## Installation

### Requirements

- Python 3

### Install Commands

```bash
git clone https://github.com/arthaudtz/gitsploit.git
cd gitsploit
pip install -r requirements.txt
```

## Basic Usage

```bash
python gitsploit.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | User/org |
| -l | Limit |

## Examples

### Example 1: Basic Usage

```bash
python gitsploit.py -u zomato
```

### Example 2: Advanced Usage

```bash
python gitsploit.py -u zomato -l 10 --type xss
```

## MITRE ATT&CK Mapping

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Services

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- GitHub API rate limits
- Search query logs

## Related Procedures

- [[procedures/Vulnerability-Discovery-with-gitSploit-on-GitHub]]

## Related Tools

- [[tools/truffleHog]]

## References

- GitHub repo
