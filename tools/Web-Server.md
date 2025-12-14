---
url: ''
tags:
  - hosting
  - c2
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.776Z'
id: fc9a0397-983a-442e-892e-75101b4c808b
validated: true
submitted: true
---
# Web-Server

**Status**: Unverified

## Overview

Generic web server (e.g., Apache, Nginx) for hosting static files and scripts, used in attacks to serve malicious payloads like JS for XSS exploitation when resources are redirected.

## Description

In security testing, web servers host attacker-controlled content to mimic legitimate assets, enabling delivery of JS, HTML, or redirects. Configurable for MIME types and rewrites to handle dynamic paths.

## Features

- Feature 1: Static file serving with custom paths
- Feature 2: URL rewriting for payload consolidation
- Feature 3: HTTPS support for evasion

## Installation

### Requirements

- Linux/Unix OS
- Root or sudo access

### Install Commands

```bash
# For Apache
sudo apt update && sudo apt install apache2
sudo systemctl start apache2
```

## Basic Usage

```bash
sudo apache2ctl -k start
```

### Common Options

| Option | Description |
|--------|-------------|
| -k start | Start server |
| config | Edit httpd.conf |

## Examples

### Example 1: Basic Usage

Place files in /var/www/html/ and access via IP.

### Example 2: Advanced Usage

Enable mod_rewrite: sudo a2enmod rewrite

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]
- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous outbound requests to unknown domains
- Server logs showing unusual file serves

## Related Procedures

- [[procedures/Set-Up-Attacker-Web-Server-for-Script-Hosting]]

## Related Tools

- [[tools/Apache]]

## References

- Related resources: Apache docs
