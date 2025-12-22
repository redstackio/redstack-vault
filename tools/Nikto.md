---
type: tool
description: >-
  Open Source (GPL) web server scanner for identifying vulnerabilities,
  misconfigurations, and outdated software.
url: 'https://cirt.net/Nikto2'
platforms:
  - Linux
  - Web
tags:
  - enumeration
  - network
  - web-applications
commands:
  - '[[commands/nikto-scan-host]]'
verified: true
validated: true
---

# Nikto

**Status**: Unverified

## Overview

Nikto is an Open Source (GPL) web server scanner which performs comprehensive tests against web servers for vulnerabilities, outdated software, misconfigurations, dangerous files, and more. It checks against a database of known issues and is commonly used in reconnaissance phases of security assessments. Note that Nikto is not stealthy and can trigger IDS/IPS alerts due to its aggressive scanning.

## Description

Nikto scans web servers by sending HTTP requests to probe for common vulnerabilities such as server leaks, missing security headers, default files, and version-specific issues. It supports HTTP and HTTPS, multiple ports, and various output formats. Ideal for initial web application enumeration but should be followed by more targeted tools like Burp Suite for deeper analysis.

## Features

- Feature 1: Comprehensive vulnerability database checks for outdated software and configurations.
- Feature 2: Detection of dangerous HTTP methods, files, and directories.
- Feature 3: Support for SSL/HTTPS, multiple hosts, and customizable scan options.
- Feature 4: Output in formats like HTML, XML, or JSON for reporting.

## Installation

### Requirements

- Perl (version 5.10 or higher)
- libwhisker2 (included or installable)

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install nikto

# Manual installation from source
wget https://cirt.net/nikto/nikto-latest.zip
unzip nikto-latest.zip
cd nikto/program
perl nikto.pl -update
```

## Basic Usage

```bash
nikto -h  # Show help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -host | Specify target host/URL |
| -port | Specify port (default 80) |
| -ssl | Force SSL mode |
| -Tuning | Tune scan for specific tests (e.g., 123 for file upload checks) |
| -output | Save output to file (e.g., -o scan.html -Format html) |

## Examples

### Example 1: Basic Usage

```bash
nikto -host http://example.com
```

### Example 2: Advanced Usage

```bash
nikto -host https://example.com -port 443 -ssl -output scan.json -Format json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of HTTP requests from a single IP to common paths (/icons/, /admin/, etc.).
- Detection method 2: User-Agent strings containing 'Nikto' or libwhisker signatures in logs.
- Detection method 3: WAF/IDS rules for aggressive probing patterns.

## Related Procedures

- [[procedures/Web-Server-Enumeration]]

## Related Tools

- [[tools/Nmap]]
- [[tools/Burp-Suite]]

## References

- Official website: https://cirt.net/Nikto2
- GitHub repository: https://github.com/sullo/nikto
