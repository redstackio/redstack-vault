---
id: tool-uuid-placeholder-001
url: 'https://github.com/lwzSoviet/NoXss.git'
tags:
  - xss
  - scanner
  - web
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.433Z'
validated: true
submitted: true
---
# NoXss

**Status**: Unverified

## Overview

NoXss is a lightweight, custom tool designed for discovering cross-site scripting (XSS) vulnerabilities through automated payload injection and response analysis. It was used to identify the reflected XSS in Python's DocXMLRPCServer, making it ideal for scanning web endpoints like XML-RPC documentation pages.

## Description

NoXss automates the testing of common XSS payloads against HTTP parameters, checking for reflections that could lead to script execution. It supports reflected, stored, and DOM-based XSS detection by parsing responses for unescaped tags. In offensive security, it's used during reconnaissance and vulnerability assessment phases for quick scans of custom or legacy web services like Python's XML-RPC servers.

## Features

- Feature 1: Automated payload fuzzing with a built-in list of XSS vectors (e.g., <script>alert(1)</script>, img onerror)
- Feature 2: Response parsing to detect reflections without manual inspection
- Feature 3: Support for GET/POST requests and customizable targets

## Installation

### Requirements

- Git
- Python 3.x
- pip for dependencies (if any)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/lwzSoviet/NoXss.git
cd NoXss
# Run setup if script provided, or directly execute
python noxss.py --help
```

## Basic Usage

```bash
noxss.py --url http://target:8000/RPC2 --param method
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-u, --url` | Target URL to scan |
| `-p, --param` | Parameter to inject payloads into |
| `-v, --verbose` | Detailed output of tests |

## Examples

### Example 1: Basic Usage

```bash
noxss.py --url http://localhost:8000/RPC2 --param method
```

### Example 2: Advanced Usage

```bash
noxss.py --url http://target.com/RPC2 --param method --payloads custom.txt -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing multiple requests with script-like payloads to the same endpoint
- Git clone activity for NoXss repository on attacker systems
- Anomalous HTTP traffic patterns from scanning tools

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
- [[XSStrike]]

## References

- Official GitHub: https://github.com/lwzSoviet/NoXss
- Related CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16935
