---
url: null
tags:
  - webserver
  - http
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.224Z'
id: 6f8301b1-c76b-4570-ad47-4ad3ba554828
validated: true
submitted: true
---
# Nginx

**Status**: Unverified

## Overview

Nginx is a high-performance web server and reverse proxy, commonly used to host static files and proxy dynamic content like PHP scripts in offensive security setups.

## Description

In SSRF attacks, Nginx hosts the initial payload (e.g., redirect scripts) on a public IP, serving requests from vulnerable apps like Bitwarden. It supports fast PHP processing via fastcgi.

## Features

- Feature 1: Lightweight HTTP server with low memory footprint
- Feature 2: Virtual host configuration for multiple domains
- Feature 3: Integration with PHP-FPM for scripting

## Installation

### Requirements

- Linux distro with apt/yum

### Install Commands

```bash
apt update && apt install nginx -y
```

## Basic Usage

```bash
nginx -t  # Test config
systemctl start nginx
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | Test configuration |
| -s reload | Reload without downtime |

## Examples

### Example 1: Basic Usage

```bash
nginx  # Start server
```
Access http://localhost.

### Example 2: Advanced Usage

Configure site in /etc/nginx/sites-available/ for PHP.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process named nginx on public ports
- Access logs showing redirects to internals
- Unauthorized configs in /etc/nginx

## Related Procedures

- [[procedures/Install-and-Configure-Nginx-Webserver]]

## Related Tools

- [[tools/Apache]]

## References

- Official docs: nginx.org
