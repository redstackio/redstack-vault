---
url: 'https://observatory.mozilla.org'
tags:
  - scan
  - headers
  - security
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.619Z'
id: 43ec1f3a-000a-4163-8bce-1cb4e507dc59
validated: true
submitted: true
---
# Mozilla-Observatory

**Status**: Unverified

## Overview

Mozilla Observatory is a free, open-source web-based tool for analyzing website security configurations, focusing on HTTP headers, TLS settings, and best practices to identify vulnerabilities like missing CSP.

## Description

It performs automated scans on domains, assigning letter grades (A-F) based on criteria from OWASP and Mozilla guidelines. In offensive security, it's used for quick reconnaissance of web apps to spot issues like clickjacking risks from absent frame protections. No local installation is required; scans are run via the web interface.

## Features

- Feature 1: Comprehensive header analysis including CSP, HSTS, and X-Frame-Options
- Feature 2: TLS/SSL configuration checks with protocol and cipher evaluations
- Feature 3: Recommendations for remediation with links to best practices

## Installation

### Requirements

- Web browser
- Internet connection

### Install Commands

No installation needed; access via browser.

## Basic Usage

Visit https://observatory.mozilla.org and enter a domain to scan.

### Common Options

| Option | Description |
|--------|-------------|
| Analyze Button | Initiates the scan |
| Privacy Mode | Scans without storing results publicly |

## Examples

### Example 1: Basic Usage

Enter 'etherscamdb.info' and click Analyze to get a report on missing CSP.

### Example 2: Advanced Usage

Use privacy mode for sensitive targets: Select 'Private Scan' before analyzing.

## Expected Output

A detailed report with grades, warnings (e.g., 'Implement CSP to protect against XSS and clickjacking'), and JSON export option.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to observatory.mozilla.org from reconnaissance IPs
- No direct detection as it's passive web access

## Related Procedures


## Related Tools

- [[tools/SSL Labs]]
- [[tools/SecurityHeaders.io]]

## References

- Official site: https://observatory.mozilla.org
- GitHub: https://github.com/mozilla/observatory
