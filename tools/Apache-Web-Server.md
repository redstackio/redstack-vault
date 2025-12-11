---
url: 'https://httpd.apache.org/'
tags:
  - web-server
  - hosting
type: tool
platforms:
  - Linux
  - Windows
description: Open-source web server software for hosting files and configuring redirects.
id: 205426b5-4213-4390-8010-d10c908cbfc3
created_at: '2025-12-11T03:47:49.863Z'
updated_at: '2025-12-11T03:47:49.863Z'
verified: false
validated: true
submitted: true
---
# Apache Web Server

**Status**: Unverified

## Overview

Apache is a widely used web server for hosting malicious scripts and configuring redirects in offensive security operations, such as XSS exploits.

## Description

Used to host JavaScript files and set up .htaccess redirects to ensure consistent delivery of payloads during CSP bypass attacks.

## Features

- Virtual hosting
- Mod_rewrite for redirects
- SSL/TLS support

## Installation

### Requirements

- Linux/Windows OS
- Package manager (apt/yum)

### Install Commands

```bash
sudo apt install apache2
```

## Basic Usage

```bash
apachectl start
```

### Common Options

| Option | Description |
|--------|-------------|
| `-k start` | Start server |
| `-k stop` | Stop server |

## Examples

### Example 1: Basic Usage

```bash
sudo apachectl start
```

### Example 2: Advanced Usage

Configure .htaccess for redirects.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[procedures/Trigger-and-Verify-XSS-Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Server logs showing rewrite rules
- Unusual hosting activity

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nginx]]

## References

- Apache official site
