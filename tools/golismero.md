---
id: 3298a1e5-6940-45c7-9fda-df5ed91ef777
type: tool
verified: true
created_at: '2019-08-28T21:17:26.434532+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-security
  - framework
  - reconnaissance
  - vulnerability-scanning
url: 'https://github.com/golismero/golismero'
validated: true
---

# golismero

**Status**: Unverified

## Overview

GoLismero is an open-source Python-based framework designed for web application security testing. It automates vulnerability scanning, integrates with popular tools like sqlmap, xsser, and openvas, and supports plugin development for custom extensions. Primarily used for reconnaissance and vulnerability detection in web environments during penetration testing.

## Description

GoLismero provides a modular framework for conducting security assessments, focusing on web applications but extensible to other scan types. Key strengths include platform independence (tested on Windows, Linux, BSD, and macOS), no native library dependencies (pure Python), and high performance compared to similar Python tools. It unifies outputs from integrated tools, maps findings to standards like CWE, CVE, and OWASP, and is designed for easy use and plugin development. While cluster deployment was planned, it's not yet implemented. Common use cases include automated web scans for SQL injection, XSS, and information leaks.

## Features

- **Modular Plugin System**: Easily develop and integrate custom plugins for specific testing needs.
- **Tool Integration**: Collects and unifies results from sqlmap (SQLi), xsser (XSS), openvas (vuln scanning), dnsrecon (DNS recon), and theharvester (OSINT).
- **Platform Independence**: Runs on multiple OS without dependencies beyond Python.
- **Output Standardization**: Generates reports mapped to security standards (CWE, CVE, OWASP).
- **Batch Processing**: Supports scanning multiple targets from files or URLs.

## Installation

### Requirements

- Python 2.7 or 3.x (pure Python, no additional libraries needed for core).
- Integrated tools (e.g., sqlmap, xsser) must be installed separately if used.

### Install Commands

```bash
# Clone from GitHub (recommended for latest)
git clone https://github.com/golismero/golismero.git
cd golismero
python setup.py install

# Or via pip (if available in PyPI)
pip install golismero

# On Kali Linux (may be pre-packaged)
apt update && apt install golismero
```

For Ubuntu/Debian: Follow the git clone method as it's not in standard repos.

For Windows/macOS: Use git clone and Python installer.

## Basic Usage

```python
golismero --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Scan a single URL |
| -f, --file | Scan targets from a file |
| --with-plugins | Include specific plugins (e.g., sqlmap) |
| --output | Specify output format (json, html, xml) |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Scan a single website for vulnerabilities:

```python
golismero -u http://example.com
```

### Example 2: Advanced Usage

Batch scan with integrated tools and HTML output:

```python
golismero -f targets.txt --with-plugins=sqlmap,xsser --output=report.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Python process named 'golismero.py' or 'golismero' with network connections to scanned targets.
- File artifacts like temporary scan outputs or logs in /tmp.
- Integrated tool signatures (e.g., sqlmap user-agent strings in HTTP requests).
- High volume of HTTP requests from a single source mimicking scanner patterns.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]]
- [[tools/xsser]]
- [[tools/openvas]]

## References

- Official GitHub: https://github.com/golismero/golismero
- Documentation: Included in repo README
- OWASP Integration Guide: https://owasp.org (for standard mappings)
