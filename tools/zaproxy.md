---
id: cbe287c4-bcfa-478d-aea9-530748188b36
type: tool
description: >-
  OWASP Zed Attack Proxy (ZAP) is an open-source, integrated penetration testing
  tool for finding vulnerabilities in web applications.
verified: true
url: 'https://www.zaproxy.org/'
tags:
  - web
  - proxy
  - scanning
  - pentest
platforms:
  - Linux
  - Windows
  - macOS
commands:
  - '[[commands/zaproxy-launch-gui]]'
  - '[[commands/zaproxy-launch-daemon]]'
  - '[[commands/zaproxy-quick-scan]]'
created_at: '2019-08-28T21:17:30.358637+00:00'
updated_at: '2024-01-01T00:00:00Z'
validated: true
---

# ZAPROXY

**Status**: Unverified

## Overview

The OWASP Zed Attack Proxy (ZAP) is a free, open-source penetration testing tool designed for finding vulnerabilities in web applications. It functions as a man-in-the-middle proxy to intercept and inspect HTTP/S messages, making it suitable for both automated and manual security testing. ZAP is accessible to users with varying levels of experience, from beginners to advanced pentesters.

## Description

ZAP supports a wide range of features for dynamic application security testing (DAST), including passive and active scanning, spidering, fuzzing, and scripting. It can be used during development to identify issues early or in production-like environments for comprehensive assessments. The tool integrates with CI/CD pipelines via its API and supports extensions for custom functionality.

## Features

- **Proxy Interception**: Intercept and modify requests/responses in real-time.
- **Automated Scanning**: Passive scanning for low-risk detection and active scanning for deeper vulnerability probing.
- **Spider and AJAX Spider**: Crawl websites to discover endpoints and parameters.
- **Fuzzer**: Test inputs for issues like XSS, SQLi, and more.
- **API Support**: REST API for automation and integration.
- **Scripting Engine**: Write custom scripts in JavaScript or Zest for advanced attacks.
- **Reporting**: Generate HTML, XML, or JSON reports with risk ratings.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- At least 2GB RAM recommended for large scans.

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update
zaproxy --version  # Verify installation
```

For Ubuntu:

```bash
sudo apt update
sudo apt install zaproxy
```

For manual installation (cross-platform):

```bash
# Download the latest release
wget https://github.com/zaproxy/zaproxy/releases/download/v2.14.0/ZAP_2.14.0_All_In_One_Installer.zip
unzip ZAP_2.14.0_All_In_One_Installer.zip
cd ZAP_2.14.0
./zap.sh  # Linux/macOS
# Or run ZAP.exe on Windows
```

## Basic Usage

```bash
zaproxy --help
```

Configure your browser to use ZAP as a proxy (localhost:8080) and browse the target application to capture traffic.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message |
| -v, --version | Show version information |
| -port <arg> | Specify proxy port (default 8080) |
| -config <key>=<value> | Set configuration options |
| -cmd | Run in command-line mode |

## Examples

### Example 1: Basic Usage

Launch ZAP and proxy browser traffic:

See [[commands/zaproxy-launch-gui]]

### Example 2: Advanced Usage

Automated daemon mode for API access:

See [[commands/zaproxy-launch-daemon]]

Quick scan of a site:

See [[commands/zaproxy-quick-scan]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (web application scanning)
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application (vulnerability discovery)

### Tactics

- [[Reconnaissance]] Reconnaissance (mapping and scanning web apps)
- [[Initial Access]] Initial Access (testing entry points)

## Detection

- Monitor for Java processes named 'zaproxy' or 'zap.jar'.
- Look for HTTP proxy traffic on non-standard ports like 8080.
- Detect unusual outbound scanning patterns or high-volume requests from testing tools.
- Enable application logging for proxy interception attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]] (alternative proxy and scanner)
- [[tools/sqlmap]] (specialized for SQL injection)
- [[tools/Nmap]] (for initial network reconnaissance)

## References

- Official documentation: https://www.zaproxy.org/docs/
- GitHub repository: https://github.com/zaproxy/zaproxy
- OWASP project page: https://owasp.org/www-project-zap/
