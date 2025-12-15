---
url: 'https://www.acunetix.com/'
tags:
  - scanner
  - web-vuln
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:22.878Z'
id: 06774483-806c-4188-ae40-0d97dca237a8
validated: true
submitted: true
---
# Acunetix

**Status**: Unverified

## Overview

Acunetix is an automated web vulnerability scanner designed to detect issues like CSRF, XSS, and SQL injection by crawling sites, analyzing forms, and testing headers.

## Description

It performs black-box scanning on web applications, identifying missing protections in forms such as the Automattic contact form. Features include form analysis, header inspection, and PoC generation for vulnerabilities. Commonly used in penetration testing for quick vuln discovery.

## Features

- Feature 1: Automated crawling and form enumeration
- Feature 2: CSRF detection via token absence checks
- Feature 3: Tech stack fingerprinting (e.g., nginx, WordPress)

## Installation

### Requirements

- Supported OS: Linux/Windows
- Java runtime for some components

### Install Commands

```bash
# Download and install via official installer
wget https://www.acunetix.com/download/acunetix_latest.sh
chmod +x acunetix_latest.sh
./acunetix_latest.sh
```

## Basic Usage

```bash
acunetix --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-t, --target` | Specify target URL |
| `-c, --config` | Load scan configuration |

## Examples

### Example 1: Basic Usage

```bash
acunetix -t http://automattic.com/contact/ -o report.html
```

### Example 2: Advanced Usage

```bash
acunetix -t http://automattic.com -c csrf-check.conf --enable-form-analysis
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Acunetix servers for updates
- Process names like acunetix_wvs.exe
- Scan logs in /var/log/acunetix

## Related Procedures


## Related Tools

- [[tools/Burp-Suite-Professional]]

## References

- Official documentation: https://www.acunetix.com/support/docs/
- Related resources: OWASP CSRF Guide
