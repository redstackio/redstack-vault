---
id: 121e43d4-6652-449c-933f-38d4f5d7b025
name: ProxyStrike
type: tool
verified: true
created_at: '2019-08-28T21:17:32.642546+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
tags:
  - web
  - proxy
  - sql-injection
  - xss
  - vulnerability-scanning
url: 'https://github.com/llaera/proxystrike'
validated: true
---

# ProxyStrike

**Status**: Unverified

## Overview

ProxyStrike is an active web application proxy designed to detect vulnerabilities such as SQL injection and XSS while browsing JavaScript-heavy web applications. It acts as a man-in-the-middle proxy, analyzing requests and parameters in the background without altering the user experience.

## Description

ProxyStrike was developed to address limitations in traditional web scanners when dealing with dynamic, JavaScript-dependent web applications. It runs as a proxy (default port 8008) that intercepts browser traffic, applies active scanning plugins for vulnerabilities, and logs results. Key capabilities include real-time vulnerability detection, request manipulation, and export of findings. It supports plugin development for custom checks and integration with alternate proxies like Tor.

## Features

- Plugin engine for custom vulnerability detection
- Request interceptor and repeater for manual testing
- Request diffing to compare responses
- Automatic crawling of web applications
- HTTP request/response history and statistics
- Parameter value analysis and signing
- SQL injection detection (based on Sqlibf port)
- XSS attack detection
- Server-Side Includes (SSI) plugin
- Attack logging and export to HTML/XML
- Support for alternate proxies (e.g., Tor)

## Installation

### Requirements

- Python 2.7 (note: legacy tool, may require Python 2 environment)
- Git

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/llaera/proxystrike.git
cd proxystrike

# For Kali Linux (may need Python 2 setup)
sudo apt update && sudo apt install python2

# For Ubuntu
sudo apt update && sudo apt install git python2

# Run setup if available (typically direct execution)
python2 proxystrike.py --help
```

## Basic Usage

```bash
python proxystrike.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p, --port | Specify listening port (default: 8008) |
| --sql | Enable SQL injection plugin |
| --xss | Enable XSS plugin |
| --tor | Use Tor as upstream proxy |
| --export | Export logs to file |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
python proxystrike.py -p 8008
```
Start the proxy and configure your browser to use localhost:8008 as the proxy.

### Example 2: Advanced Usage

```bash
python proxystrike.py -p 8008 --sql --xss --tor
```
Run with plugins enabled and Tor integration for anonymized scanning.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on non-standard ports (e.g., 8008)
- Python processes with network listening (e.g., via netstat or ss)
- Log files or exports containing vulnerability scans
- Browser proxy configurations pointing to local tools

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

- Official GitHub: https://github.com/llaera/proxystrike
- Documentation in repository README
