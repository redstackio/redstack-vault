---
type: tool
description: >-
  Grabber is a portable Python-based web application vulnerability scanner
  designed for small websites, detecting XSS, SQL Injection, file inclusions,
  and other common web vulnerabilities.
url: 'https://github.com/ryuzaki/Grabber'
tags:
  - web-scanning
  - vulnerability-assessment
  - xss
  - sqli
  - file-inclusion
platforms:
  - Linux
  - Windows
  - macOS
commands:
  - '[[commands/grabber-basic-scan]]'
  - '[[commands/grabber-xss-specific-scan]]'
  - '[[commands/grabber-sqli-scan]]'
verified: true
validated: true
---

# grabber

**Status**: Unverified

## Overview

Grabber is a simple, portable web application scanner tailored for auditing small websites like personal pages or forums. It identifies vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection (including blind variants), file inclusions, backup file exposures, basic AJAX interactions, PHP application analysis via PHP-SAT, JavaScript code quality checks, and session-based statistics. While not optimized for large-scale applications due to performance limitations, it's adaptable for targeted security assessments.

## Description

Grabber operates by crawling and testing web pages for common injection flaws and misconfigurations. It uses modular engines for different vulnerability types, making it suitable for offensive security testing in controlled environments. The tool generates reports on potential issues and can integrate with proxies for traffic interception. It's particularly useful for quick scans during penetration testing phases focused on web apps.

## Features

- **Cross-Site Scripting (XSS)**: Detects reflected, stored, and DOM-based XSS vulnerabilities.
- **SQL Injection (SQLi)**: Scans for standard and blind SQLi, including time-based and boolean variants.
- **File Inclusion**: Checks for Local and Remote File Inclusion (LFI/RFI) paths.
- **Backup Files Check**: Identifies exposed backup or configuration files (e.g., .bak, .old).
- **Simple AJAX Check**: Parses JavaScript to extract and test AJAX endpoints for parameters.
- **Hybrid Analysis/PHP-SAT**: Performs static analysis on PHP code for logical flaws using SAT solvers.
- **JavaScript Source Code Analyzer**: Evaluates JS quality and potential issues with JavaScript Lint integration.
- **Session Statistics**: Generates logs of [session_id, timestamp] for post-scan analysis.

## Installation

### Requirements

- Python 2.7 (note: legacy tool, may require virtualenv for compatibility)
- pip-installed dependencies: requests, beautifulsoup4, jsbeautifier (install via requirements.txt if available)
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ryuzaki/Grabber.git
cd Grabber

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# No formal setup.py; run directly with python
```

For modern systems, consider using a Python 2 virtual environment:

```bash
virtualenv -p python2 grabber_env
source grabber_env/bin/activate
pip install requests beautifulsoup4
```

## Basic Usage

```python
python grabber.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Target URL to scan |
| -e, --engine | Specify scanning engine (e.g., xss, sqli, inclusion) |
| -p, --proxy | HTTP proxy for requests (e.g., http://127.0.0.1:8080) |
| -t, --threads | Number of threads for faster scanning |
| -o, --output | Output file for results |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```python
python grabber.py -u http://example.com
```

This runs a full basic scan on the target site.

### Example 2: Advanced Usage

```python
python grabber.py -u http://example.com -e xss -p http://127.0.0.1:8080 -t 3 -o results.txt
```

Scans specifically for XSS, routes through a proxy, uses 3 threads, and saves output.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP requests patterns to web servers (e.g., injection payloads in GET/POST).
- Python processes named 'grabber.py' or network traffic from known scanner user-agents.
- Log entries for backup file accesses or AJAX endpoint probes.
- Integration with proxies like Burp Suite may show intercepted scanner traffic.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/ZAP]]

## References

- Official GitHub: https://github.com/ryuzaki/Grabber
- Documentation: Included in repo README
