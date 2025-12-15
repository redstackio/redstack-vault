---
id: tool-uuid-1
url: ''
tags:
  - hosting
  - poc-delivery
type: tool
verified: false
platforms:
  - Linux
  - Microsoft Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:31.231Z'
validated: true
submitted: true
---
# Generic-Web-Server

**Status**: Unverified

## Overview

A generic web server tool for hosting static files like HTML PoCs in security testing, commonly used to deliver malicious content without specifying a particular implementation (e.g., Apache, nginx, or Python's http.server).

## Description

This represents any basic HTTP server capable of serving files over port 80/443. In offensive operations, it's used to host exploit PoCs for download by targets, enabling attacks like the Brave scheme bypass by providing accessible URLs for HTML files with embedded malicious links.

## Features

- Feature 1: Simple file serving for static content like HTML/JS
- Feature 2: Configurable ports and directories
- Feature 3: Logging for access monitoring

## Installation

### Requirements

- Operating system with Python, Apache, or equivalent
- Network access for binding ports

### Install Commands

```bash
# For Python simple server (no install needed)
python -m http.server 8000

# For Apache (on Ubuntu)
sudo apt install apache2
sudo systemctl start apache2
```

## Basic Usage

```bash
python -m http.server 8000
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p PORT` | Specify port (default 8000) |
| `-d DIR` | Serve from specific directory |

## Examples

### Example 1: Basic Usage

```bash
cd /path/to/poc && python -m http.server 8000
```
Access at http://attacker-ip:8000/braveRCE.html

### Example 2: Advanced Usage

```bash
nginx -c /etc/nginx/nginx.conf  # With config for HTTPS
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP traffic from unknown IPs serving HTML
- Server logs showing PoC file requests
- Network scans revealing open web ports on attacker hosts

## Related Procedures

- [[procedures/Host-and-Deliver-Brave-PoC-HTML]]

## Related Tools

- [[Apache HTTP Server]]
- [[nginx]]

## References

- Python docs: https://docs.python.org/3/library/http.server.html
- General web hosting guides
