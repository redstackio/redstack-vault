---
id: tool-apache-001
url: 'https://httpd.apache.org/'
tags:
  - web-server
  - logging
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.680Z'
validated: true
submitted: true
---
# Apache-Web-Server

**Status**: Unverified

## Overview

Apache HTTP Server is an open-source web server used to host test pages and capture incoming requests during SSRF exploitation testing.

## Description

In offensive security, Apache is configured to log access requests, allowing verification of SSRF by observing traffic from victim servers like Imgur to attacker paths.

## Features

- Feature 1: Comprehensive access and error logging
- Feature 2: Modular configuration for custom virtual hosts
- Feature 3: Support for HTTPS and various modules (e.g., mod_rewrite)

## Installation

### Requirements

- Linux OS (e.g., Ubuntu)
- Root or sudo access

### Install Commands

```bash
sudo apt update
sudo apt install apache2
```

## Basic Usage

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | N/A (systemctl manages service) |
| Config file | /etc/apache2/apache2.conf |

## Examples

### Example 1: Basic Usage

```bash
sudo apache2ctl configtest
sudo systemctl restart apache2
```

### Example 2: Advanced Usage

```bash
# Enable logging module
sudo a2enmod log_config
sudo systemctl restart apache2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port 80/443 listening
- Log files in /var/log/apache2/
- Process: httpd or apache2

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[nginx]]
- [[lighttpd]]

## References

- Official documentation: https://httpd.apache.org/docs/
- Related resources: Apache logging guide
