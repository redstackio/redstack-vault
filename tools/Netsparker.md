---
id: tool-netsparker-001
url: 'https://www.netsparker.com/'
tags:
  - dast
  - scanner
  - xss
  - web-vuln
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.903Z'
validated: true
submitted: true
---
# Netsparker

**Status**: Unverified

## Overview

Netsparker is a dynamic application security testing (DAST) tool designed for automated vulnerability scanning of web applications, particularly effective for detecting XSS, SQLi, and other injection flaws in CMS like Concrete5.

## Description

It performs black-box scanning by crawling sites and injecting test payloads, proofing exploits with automatic verification to reduce false positives. In offensive security, it's used for initial vuln discovery in admin interfaces, supporting authenticated scans and custom payload tuning.

## Features

- Feature 1: Automated proof-of-exploit for confirmed vulns like XSS alerts
- Feature 2: Support for complex apps with JavaScript rendering
- Feature 3: Reporting with remediation guidance and CI/CD integration

## Installation

### Requirements

- Java Runtime Environment (for some components)
- Supported OS: Windows primary, Linux/macOS via cloud

### Install Commands

```bash
# Download and install via official installer (Windows)
# For Linux, use cloud version or Docker if available
wget https://www.netsparker.com/download -O netsparker.deb && sudo dpkg -i netsparker.deb
```

## Basic Usage

```bash
netsparker scan --url https://target.com --profile standard
```

### Common Options

| Option | Description |
|--------|-------------|
| `--url` | Target website URL |
| `--tests xss` | Enable specific test categories |
| `--auth` | Provide login credentials |

## Examples

### Example 1: Basic Usage

```bash
netsparker scan --url https://target.com/concrete5.7.3.1/ --scope /dashboard/
```

### Example 2: Advanced Usage

```bash
netsparker scan --url https://target.com --tests xss, injection --output report.html --auth user:pass
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Netsparker cloud scanners
- High volume of anomalous requests with test payloads
- Log entries for repeated XSS-like queries

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/OWASP-ZAP]]

## References

- Official documentation: https://www.netsparker.com/support/
- Related resources: OWASP Testing Guide
