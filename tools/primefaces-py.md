---
url: 'https://github.com/pimps/CVE-2017-1000486'
tags:
  - rce
  - exploit
  - primefaces
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:31.153Z'
id: 045c9165-f046-48b7-956a-f8030d7dd67b
validated: true
submitted: true
---
---

# primefaces-py

**Status**: Unverified

## Overview

primefaces.py is a Python-based exploit script designed to target CVE-2017-1000486, a remote code execution vulnerability in PrimeFaces 5.x versions, specifically exploiting weak encryption in the EL parser of JSF applications. It is commonly used in penetration testing to demonstrate RCE on vulnerable web servers.

## Description

The tool sends crafted HTTP requests to the target application, injecting malicious EL expressions that bypass encryption and execute system commands. It supports specifying the target URL and command payload, making it straightforward for verifying exploitation. In offensive security, it's used for initial access to public-facing Java web apps, potentially leading to full server compromise.

## Features

- Feature 1: EL injection payload generation for PrimeFaces 5.3.6
- Feature 2: Command execution via HTTP POST requests
- Feature 3: Simple CLI interface for targeting URLs and payloads

## Installation

### Requirements

- Python 2.7 or 3.x
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/pimps/CVE-2017-1000486.git
cd CVE-2017-1000486
```

## Basic Usage

```bash
python primefaces.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Target website URL |
| -c, --command | Command to execute on the server |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
python primefaces.py -u "https://target-dod-website.com" -c "whoami"
```

### Example 2: Advanced Usage

```bash
python primefaces.py -u "https://vulnerable-app.com" -c "id; uname -a"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network logs showing POST requests with EL patterns like '#{...}'
- Detection method 2: Server access logs with unexpected command executions (e.g., 'whoami')

## Related Procedures

- [[procedures/Exploit-PrimeFaces-RCE-via-EL-Injection]]

## Related Tools

- [[Metasploit]]
- [[Burp Suite]]

## References

- Official GitHub: https://github.com/pimps/CVE-2017-1000486
- CVE Details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-1000486
