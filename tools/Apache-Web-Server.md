---
id: tool-apache-server
url: 'https://httpd.apache.org/'
tags:
  - web-server
  - logging
  - ssrf
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.808Z'
validated: true
submitted: true
---
# Apache Web Server

**Status**: Unverified

## Overview

Apache HTTP Server is an open-source web server used here to host test files and capture incoming SSRF requests via access logs, verifying exploitation by logging requests from victim servers like Imgur.

## Description

In offensive security, Apache serves as a controllable endpoint for SSRF testing, logging IP origins, methods (HEAD/GET), and paths to confirm proxied requests. Configuration focuses on access logging for paths like /.testing/xss.html.

## Features

- Feature 1: Detailed access logging for request tracking
- Feature 2: Support for virtual hosts and custom paths
- Feature 3: Integration with tools like mod_security for advanced logging

## Installation

### Requirements

- Linux/Unix system or Windows with compatible setup
- Root/admin privileges

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install apache2

# On CentOS/RHEL
sudo yum install httpd
sudo systemctl start httpd
```

## Basic Usage

```bash
sudo apachectl start
sudo apachectl configtest
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for apachectl |
| `-k start` | Start the server |
| `-k graceful` | Graceful restart |

## Examples

### Example 1: Basic Usage

```bash
sudo apache2ctl start
# Host files in /var/www/html/.testing/
```

### Example 2: Advanced Usage

```bash
# Configure logging in /etc/apache2/sites-available/000-default.conf
LogFormat "%h %l %u %t \"%r\" %>s %b" common
CustomLog /var/log/apache2/crowdshield_access.log common
sudo a2enmod rewrite && sudo systemctl restart apache2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outbound requests to attacker domains from web apps
- Log analysis for high-volume HEAD requests from cloud IPs
- Network monitoring for SSRF patterns

## Related Procedures

- [[procedures/Craft-and-Trigger-Imgur-SSRF-Request]]
- [[procedures/Verify-SSRF-Exploitation-via-Server-Logs]]

## Related Tools

- [[nginx]]
- [[Python SimpleHTTPServer]]

## References

- Official documentation: https://httpd.apache.org/docs/
- Logging guide: https://httpd.apache.org/docs/2.4/logs.html
