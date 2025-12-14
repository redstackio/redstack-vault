---
url: 'https://sqlmap.org/'
tags:
  - sql-injection
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.458Z'
id: 4bfca160-3dba-4379-a651-b5beb1832372
validated: true
submitted: true
---
# SQLMap

**Status**: Unverified

## Overview

SQLMap is an open-source automated tool for detecting and exploiting SQL injection flaws, commonly used in penetration testing to extract database data from vulnerable web applications.

## Description

SQLMap supports a wide range of databases (MySQL, PostgreSQL, Oracle, etc.) and injection techniques, including error-based, blind, and time-based. In offensive security, it's used to quickly assess and exploit web vulnerabilities like those on the Sony website, automating payload injection, database enumeration, and data dumping.

## Features

- Feature 1: Automatic detection of injection points and types
- Feature 2: Database enumeration (users, tables, columns, data dumping)
- Feature 3: Support for POST, GET, headers, and cookie injections

## Installation

### Requirements

- Python 3.x
- Git

### Install Commands

```bash
# Clone from GitHub
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd sqlmap-dev

# Or via pip
pip install sqlmap
```

## Basic Usage

```bash
sqlmap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target URL for testing |
| `--dbs` | Enumerate databases |
| `--batch` | Non-interactive execution |
| `-v, --verbose` | Verbosity level (0-6) |

## Examples

### Example 1: Basic Usage

```bash
sqlmap -u "http://target.com/page?id=1" --dbs
```

### Example 2: Advanced Usage

```bash
sqlmap -u "http://sony-website.com/███████?id=1" --dbs --level=5 --risk=3 --batch
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic with repeated anomalous HTTP requests containing SQL payloads
- Server logs showing multiple failed SQL queries or error patterns
- Process monitoring for 'sqlmap.py' execution on compromised hosts

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[OWASP ZAP]]

## References

- Official documentation: https://sqlmap.org/
- GitHub: https://github.com/sqlmapproject/sqlmap
