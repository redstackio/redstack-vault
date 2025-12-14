---
id: tool-acunetix
url: 'https://www.acunetix.com/'
tags:
  - scanning
  - web
  - xss
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.476Z'
validated: true
submitted: true
---
# Acunetix

**Status**: Unverified

## Overview

Acunetix is an automated web vulnerability scanner designed for discovering issues like XSS, SQLi, and CSRF in web applications and APIs. It's commonly used in penetration testing to identify flaws like the content-sniffing XSS in Khan Academy.

## Description

Acunetix performs dynamic application security testing (DAST) by crawling sites, injecting payloads into forms and parameters, and analyzing responses for vulnerabilities. For XSS, it tests reflection and execution across contexts, including API endpoints. In offensive operations, it's used for initial recon and vuln confirmation before manual exploitation.

## Features

- Feature 1: Advanced crawler for JavaScript-heavy sites and APIs
- Feature 2: Built-in payload library for XSS, including obfuscated variants
- Feature 3: Integration with CI/CD for automated scanning and reporting

## Installation

### Requirements

- Supported OS: Windows, Linux, macOS
- .NET Framework (Windows) or Mono (Linux)

### Install Commands

```bash
# Download from official site and run installer
# For Linux: wget https://www.acunetix.com/... && sudo dpkg -i acunetix.deb
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
| `-p, --profile` | Select scan profile (e.g., XSS-focused) |

## Examples

### Example 1: Basic Usage

```bash
acunetix -t https://www.khanacademy.org -p standard
```

### Example 2: Advanced Usage

```bash
acunetix -t https://www.khanacademy.org/api/internal -p high-risk --modules xss,api
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic with Acunetix user-agent strings
- High volume of requests with varying payloads to the same endpoints
- Log entries for scan-like probing patterns

## Related Procedures

- [[procedures/Scan-for-XSS-Vulnerabilities-with-Acunetix]]

## Related Tools

- [[Burp Suite]]
- [[OWASP ZAP]]

## References

- Official documentation: https://www.acunetix.com/support/docs/
- Related resources: HackerOne reports on XSS discoveries
