---
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-proxy
  - vulnerability-scanner
  - interception
url: 'http://www.parosproxy.org/'
validated: true
---

# Paros

**Status**: Unverified

## Overview

Paros is an open-source Java-based HTTP/HTTPS proxy designed for assessing web application vulnerabilities. It acts as a man-in-the-middle proxy, allowing security testers to intercept, inspect, modify, and replay HTTP/HTTPS messages on-the-fly. Commonly used in penetration testing for identifying issues like XSS, SQL injection, and authentication flaws.

## Description

Paros Proxy provides a comprehensive suite of tools for web application security testing, including traffic interception, request/response editing, automated spidering for site mapping, and passive/active scanning for common vulnerabilities. It supports proxy chaining, client certificates for authenticated testing, and fuzzy boundary testing for input validation issues. While primarily GUI-driven, it integrates well with browsers and other tools via standard proxy settings (default port 8080). It's particularly useful for manual testing workflows similar to Burp Suite but with a focus on ease of use for beginners.

## Features

- **Traffic Interception**: View and modify HTTP/HTTPS requests and responses in real-time.
- **Spider**: Automated crawling to map application structure and discover hidden endpoints.
- **Scanner**: Intelligent active and passive scanning for XSS, SQL injection, and other OWASP Top 10 vulnerabilities.
- **Proxy Chaining**: Route traffic through upstream proxies for evading restrictions.
- **Client Certificates**: Support for mutual TLS authentication.
- **Session Management**: Save and load testing sessions for repeatability.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- At least 512MB RAM for GUI operation.

### Install Commands

```bash
# Download the latest Paros JAR from the official site
wget https://downloads.sourceforge.net/project/paros/1.2/paros-3.6.7.jar

# Or on Windows/macOS, download via browser from http://www.parosproxy.org/

# No installation required; run directly with Java
```

For HTTPS interception, export the Paros CA certificate from the GUI (Tools > Options > Miscellaneous > Dynamic SSL Certificates) and import it into the browser or system trust store.

## Basic Usage

```bash
# Launch Paros (replace with actual JAR path)
java -jar paros.jar
```

Once launched, configure your browser to use localhost:8080 as the proxy. Browse the target application to begin intercepting traffic.

### Common Options

| Option | Description |
|--------|-------------|
| `-port <N>` | Set proxy listening port (default: 8080) |
| `-host <IP>` | Bind to specific IP address |
| `-help` | Show usage information |

## Examples

### Example 1: Basic Usage

```bash
java -jar paros-3.6.7.jar
```
Launch the GUI, set browser proxy to 127.0.0.1:8080, and navigate to the target site to intercept requests.

### Example 2: Advanced Usage

```bash
java -port 8090 -jar paros-3.6.7.jar
```
Launches on port 8090 for use with tools requiring custom ports; chain with upstream proxies via GUI settings.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for interception during testing)
- [[Active Scanning]] Active Scanning (via built-in scanner)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic routed through non-standard proxy ports (e.g., 8080).
- Presence of Paros CA certificate in browser/system trust stores.
- Java processes running paros.jar on defender systems (via process monitoring).
- Unusual HTTP requests with modified headers or payloads indicative of manual tampering.

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

- Official documentation: http://www.parosproxy.org/docs/
- SourceForge project: https://sourceforge.net/projects/paros/
- OWASP integration guide: https://owasp.org/www-community/tools/Paros_Proxy
