---
url: 'https://sqlmap.org'
tags:
  - sql-injection
  - exploitation
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Automated SQL injection detection and exploitation tool
id: 0cb3c74d-fcaa-4e25-b356-a819dd464e96
created_at: '2025-12-11T06:10:30.689Z'
updated_at: '2025-12-11T06:10:30.689Z'
verified: false
validated: true
submitted: true
---
# sqlmap

**Status**: Unverified

## Overview

sqlmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over database servers.

## Description

It supports a wide range of database management systems and includes features for database fingerprinting, data fetching, and access to the underlying file system.

## Features

- Feature 1: Automatic SQL injection detection
- Feature 2: Support for multiple DBMS
- Feature 3: Tamper scripts for evasion

## Installation

### Requirements

- Python 3.x
- Git

### Install Commands

```bash
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
```

## Basic Usage

```bash
python sqlmap.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--tamper` | Use tamper script |

## Examples

### Example 1: Basic Usage

```bash
python sqlmap.py -u "http://target.com/vuln.php?id=1"
```

### Example 2: Advanced Usage

```bash
python sqlmap.py -u "http://target.com" --tamper htmlencode --dbms mssql
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Sniffing]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP traffic patterns
- Detection method 2: sqlmap user-agent in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[ZAP]]

## References

- Official documentation: https://sqlmap.org
- Related resources: GitHub repository
