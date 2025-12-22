---
id: b4d23246-d743-4536-816a-a70b19bc5245
type: tool
verified: true
created_at: '2019-08-28T21:17:36.280724+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - mitm
  - ssl
  - tls
  - proxy
  - testing
  - adversary-in-the-middle
url: 'https://github.com/sslcaudit/sslcaudit'
validated: true
---

# sslcaudit

**Status**: Unverified

## Overview

SSLCAudit is a utility designed to automate the testing of SSL/TLS clients for their resistance to Man-in-the-Middle (MITM) attacks. It functions as a proxy that intercepts client connections, allowing security testers to evaluate how well applications, thick clients, mobile apps, or appliances validate certificates and handle intercepted traffic over TCP-based SSL/TLS connections.

## Description

The primary goal of SSLCAudit is to simulate MITM scenarios by positioning itself between the client and server, enabling testers to identify weaknesses in certificate validation, hostname verification, and other SSL/TLS security mechanisms. This tool is particularly useful in penetration testing for non-browser applications that communicate over encrypted channels, helping to uncover vulnerabilities that could allow unauthorized interception of sensitive data.

## Features

- Feature 1: Acts as a transparent MITM proxy for SSL/TLS connections, automatically handling certificate replacement.
- Feature 2: Supports testing of custom certificates and keys to mimic real-world attack scenarios.
- Feature 3: Logs client responses to intercepted connections, providing detailed audit trails of validation failures.
- Feature 4: Compatible with various client types, including desktop applications, mobile apps, and embedded devices.
- Feature 5: Options for insecure mode to bypass certain validations during testing.

## Installation

### Requirements

- Python 2.7 or 3.x
- Twisted library (pip install twisted)
- OpenSSL for certificate generation (if using custom certs)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/sslcaudit/sslcaudit.git
cd sslcaudit

# Install dependencies
pip install -r requirements.txt

# For Ubuntu/Debian (if needed)
sudo apt update && sudo apt install python3-pip python3-twisted
```

On Kali Linux, it may require manual setup as it's not pre-packaged; follow the git clone steps.

## Basic Usage

```bash
tool-name --help
```

Run `python sslcaudit.py --help` to see all options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --verbose | Enable verbose logging for detailed output |
| -insecure | Disable certain security checks during proxy operation |
| -logfile | Specify a file for logging audit results |

## Examples

### Example 1: Basic Usage

```python
python sslcaudit.py -host targetapp.com -port 443
```

This starts the proxy listening for connections to targetapp.com on port 443, simulating a MITM attack.

### Example 2: Advanced Usage

```python
python sslcaudit.py -host targetapp.com -port 443 -cert custom.crt -key custom.key -insecure -logfile mitm_audit.log
```

Uses custom credentials and logs results to a file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Forge Web Credentials]] Forge Web Credentials

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic or certificate mismatches in network logs.
- Detection method 2: Presence of Python processes with Twisted library loading custom certs.
- Detection method 3: Log entries showing intercepted SSL connections on non-standard ports.

## Related Procedures

- [[procedures/Test-SSL-TLS-Client-MITM-Resistance]]

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/mitmproxy]]

## References

- Official GitHub: https://github.com/sslcaudit/sslcaudit
- Documentation: README in the repository
- Related: SSL/TLS testing best practices from OWASP
