---
id: 63fb49d7-99ac-42df-ad40-5a207e38e88f
type: tool
verified: true
created_at: '2019-08-28T21:17:41.459045+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - proxy
  - redirection
  - evasion
  - web-server
url: 'https://github.com/example/now-you-see-me'
commands:
  - '[[commands/now-you-see-me-start-basic-server]]'
  - '[[commands/now-you-see-me-configure-ssl]]'
validated: true
---

# now-you-see-me

**Status**: Unverified

## Overview

now-you-see-me is a lightweight pass-thru web server designed for traffic redirection in security testing and red team operations. It acts as a transparent proxy, forwarding incoming HTTP/HTTPS requests to a specified target while allowing for logging, modification, or evasion of network controls. Common use cases include simulating legitimate traffic, bypassing web application firewalls (WAFs), or redirecting C2 communications during engagements.

## Description

The tool creates a simple server that listens on a local port and relays all traffic to a backend target URL. It supports both plain HTTP and SSL/TLS configurations, making it versatile for testing proxy behaviors, intercepting requests, or chaining with other tools like Burp Suite. Unlike full-featured proxies, now-you-see-me focuses on minimal overhead and ease of deployment, ideal for quick setups in lab environments or field operations. It logs requests by default for analysis and can be extended with custom scripts for response manipulation.

## Features

- Feature 1: Transparent HTTP/HTTPS forwarding with low latency
- Feature 2: Configurable logging levels for request/response inspection
- Feature 3: SSL/TLS support for secure redirection
- Feature 4: Simple command-line interface for rapid deployment
- Feature 5: Cross-platform compatibility (Python-based)

## Installation

### Requirements

- Python 3.6+
- pip for dependency installation
- OpenSSL for SSL configurations (optional)

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/now-you-see-me.git
cd now-you-see-me

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update && sudo apt install python3-pip git
pip3 install -r requirements.txt

# For Windows (using pip)
pip install -r requirements.txt
```

## Basic Usage

```bash
python now_you_see_me.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| --listen-port PORT | Specify the local listening port (default: 8080) |
| --target-url URL | Set the target URL for forwarding |
| --ssl-cert CERT | Path to SSL certificate for HTTPS |
| --ssl-key KEY | Path to SSL private key |
| --log-level LEVEL | Set logging verbosity (debug, info, warn) |

## Examples

### Example 1: Basic Usage

Start a simple HTTP proxy forwarding to an internal server:

```bash
python now_you_see_me.py --listen-port 8080 --target-url http://192.168.1.100
```
Access http://localhost:8080 to see redirected traffic.

### Example 2: Advanced Usage

Enable SSL and debug logging:

```bash
python now_you_see_me.py --listen-port 8443 --target-url https://api.internal --ssl-cert cert.pem --ssl-key key.pem --log-level debug
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual inbound connections to non-standard ports (e.g., 8080, 8443) with forwarding patterns
- Detection method 2: Python processes with network binding and high outbound traffic to internal targets
- Detection method 3: Log analysis for proxy-like request patterns without corresponding application logs

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
- [[tools/ngrok]]

## References

- Official GitHub repository: https://github.com/example/now-you-see-me
- Python Flask documentation for underlying server (if applicable)
- Related resources: OWASP Proxy Testing Guide
