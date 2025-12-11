---
url: 'https://sqlmap.org/'
tags:
  - sqli
  - exploitation
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Automatic SQL injection and database takeover tool
id: a4d19503-69ec-488b-81eb-236e358a9853
created_at: '2025-12-11T03:47:39.529Z'
updated_at: '2025-12-11T03:47:39.529Z'
verified: false
validated: true
submitted: true
---
# sqlmap

**Status**: Unverified

## Overview

sqlmap automates the detection and exploitation of SQL injection vulnerabilities.

## Description

It supports various databases and techniques for injecting payloads and extracting data.

## Features

- Feature 1: Automatic detection
- Feature 2: Data dumping
- Feature 3: OS command execution

## Installation

### Requirements

- Python installed

### Install Commands

```bash
git clone https://github.com/sqlmapproject/sqlmap.git
```

## Basic Usage

```bash
python sqlmap.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-u` | Target URL |

## Examples

### Example 1: Basic Usage

```bash
python sqlmap.py -u "https://target.com/vuln"
```

### Example 2: Advanced Usage

```bash
python sqlmap.py -u "https://target.com/vuln" --dump-all
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Anomalous SQL queries in logs
- Detection method 2: Known sqlmap User-Agent

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #burpsuite
- #zaproxy

## References

- Official sqlmap website
