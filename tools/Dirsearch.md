---
url: 'https://github.com/maurosoria/dirsearch'
tags:
  - brute-force
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.170Z'
id: 2f37cc3a-4cf6-4bdb-8c7d-b89198c47605
validated: true
submitted: true
---
# Dirsearch

**Status**: Unverified

## Overview

Dirsearch is a Python-based command-line tool for brute forcing directories and files on web servers.

## Description

It supports multithreading, custom wordlists, and extension fuzzing, useful for discovering hidden endpoints.

## Features

- Feature 1: Support for multiple extensions
- Feature 2: Exclusion of status codes
- Feature 3: Custom headers and recursion

## Installation

### Requirements

- Python 3

### Install Commands

```bash
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip install -r requirements.txt
```

## Basic Usage

```bash
python3 dirsearch.py -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | Target URL |
| -w | Wordlist |
| -t | Threads |

## Examples

### Example 1: Basic Usage

```bash
python3 dirsearch.py -u https://example.com/
```

### Example 2: Advanced Usage

With extensions and headers as in extraction.

## MITRE ATT&CK Mapping

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

- Rate limiting on web servers
- WAF rules for brute force patterns

## Related Procedures

- [[procedures/Reconnaissance-and-Exposed-Git-Discovery]]

## Related Tools

- [[tools/Gobuster]]

## References

- GitHub repo
