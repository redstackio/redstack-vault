---
url: >-
  https://www.vidocsecurity.com/blog/2022-summary-how-we-made-120k-bug-bounty-in-a-year/
tags:
  - recon
  - swagger-ui
type: tool
platforms:
  - Linux
  - Windows
  - macOS
descriptionⅈescription: Custom module for detecting Swagger-UI instances across companies
id: 71d5a06a-d374-4da0-b2d6-191c4b114f67
created_at: '2025-12-13T23:56:20.447Z'
updated_at: '2025-12-13T23:56:20.447Z'
verified: false
validated: true
submitted: true
---
# Custom Swagger UI Detection Module

**Status**: Unverified

## Overview

A custom-built tool for scanning and detecting exposed Swagger-UI instances across multiple domains at scale, used in bug bounty and security research to identify potential vulnerabilities like XSS.

## Description

This module automates the process of searching for Swagger-UI endpoints by scanning domain lists and checking for characteristic responses. It's designed for efficiency in large-scale reconnaissance, helping identify old or misconfigured instances that may be exploitable.

## Features

- Scalable domain scanning
- Pattern-based detection of Swagger-UI
- Output of detected endpoints for further analysis

## Installation

### Requirements

- Python 3.x
- Requests library

### Install Commands

```bash
pip install requests
# Clone or download the custom script from the blog reference
```

## Basic Usage

```bash
python detect_swagger.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d, --domain` | Target domain to scan |
| `-o, --output` | Output file for results |

## Examples

### Example 1: Basic Usage

```bash
python detect_swagger.py -d example.com -o results.txt
```

### Example 2: Advanced Usage

```bash
python detect_swagger.py -d list.txt -o results.txt --threads 10
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual traffic patterns to /doc/ or /swagger paths
- High volume of requests from single IP

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[ffuf]]
- [[dirsearch]]

## References

- https://www.vidocsecurity.com/blog/2022-summary-how-we-made-120k-bug-bounty-in-a-year/
