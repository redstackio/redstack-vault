---
id: tool-local-web-server
url: ''
tags:
  - hosting
  - exfiltration
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.181Z'
description: >-
  Generic local HTTP server for hosting scripts to receive exfiltrated data
  during attacks.
validated: true
submitted: true
---
# Local-Web-Server

**Status**: Unverified

## Overview

A local web server hosts PHP or other scripts to capture data exfiltrated from remote exploits, such as XSS-driven cookie theft, typically on localhost.

## Description

Configured at http://localhost/test.php, this server uses PHP's built-in capabilities or tools like Apache to serve dynamic content. In security testing, it's essential for simulating attacker-controlled endpoints without external exposure. Basic configuration involves starting the server and placing scripts in the document root.

## Features

- Feature 1: Serves static and dynamic files
- Feature 2: Handles GET/POST requests
- Feature 3: Logs incoming traffic for analysis

## Installation

### Requirements

- PHP or Apache installed

### Install Commands

```bash
# Use PHP built-in (no install needed if PHP present)
# Or install Apache
sudo apt install apache2
sudo systemctl start apache2
```

## Basic Usage

```bash
php -S localhost:80
```

### Common Options

| Option | Description |
|--------|-------------|
| `-S host:port` | Bind to address and port |
| `-t dir` | Document root directory |

## Examples

### Example 1: Basic Usage

```bash
php -S localhost:80
```

### Example 2: Advanced Usage

```bash
php -S 127.0.0.1:8080 -t ./webroot
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Localhost traffic in network logs
- Unexpected server processes

## Related Procedures

- [[procedures/Set-Up-Local-PHP-Server-for-Cookie-Capture]]

## Related Tools

- [[tools/PHP]]
- [[nginx]]

## References

- Related resources: PHP Server Documentation
