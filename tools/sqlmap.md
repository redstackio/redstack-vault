---
url: ''
tags:
  - sqli
  - automated-exploit
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.209Z'
id: 3efd8ca0-86dc-460b-95d0-08d13cd003d1
validated: true
submitted: true
---
# sqlmap

**Status**: Unverified

## Overview

SQLMap is an open-source automated tool for detecting and exploiting SQL injection flaws, supporting various techniques like error-based, union-based, and time-based for database takeover.

## Description

It excels in web app pentests by analyzing HTTP requests, injecting payloads, and extracting data from backends like MySQL. For Revive Adserver, it targets the 'keyword' parameter to dump databases, tables, and execute commands.

## Features

- Feature 1: Support for multiple injection techniques (error, blind, time-based)
- Feature 2: Database enumeration and data dumping
- Feature 3: HTTP request file loading with authentication handling

## Installation

### Requirements

- Python 3+

### Install Commands

```bash
# Git clone and install
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd sqlmap-dev
python sqlmap.py --help
```

## Basic Usage

```bash
sqlmap -u "http://target.com/vuln.php?id=1" --dbs
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Load request from file |
| `--dbs` | Enumerate databases |
| `--batch` | Non-interactive mode |

## Examples

### Example 1: Basic Usage

```bash
sqlmap -r testsql.txt --dbs
```

### Example 2: Advanced Usage

```bash
sqlmap -r testsql.txt --dbs --tables --dump
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious SQL payloads in app logs
- Unusual database query delays
- Network requests with encoded payloads

## Related Procedures

- [[procedures/Exploit-SQL-Injection-with-SQLMap]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official GitHub: https://github.com/sqlmapproject/sqlmap
