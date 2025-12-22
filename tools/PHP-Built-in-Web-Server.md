---
id: tool-php-builtin-server-001
url: 'https://www.php.net/manual/en/features.commandline.webserver.php'
tags:
  - php
  - server
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:09.938Z'
validated: true
submitted: true
---
# PHP-Built-in-Web-Server

**Status**: Unverified

## Overview

The PHP built-in web server is a lightweight development server included with PHP for hosting applications without needing Apache or Nginx, ideal for testing vulnerabilities like session upload progress issues.

## Description

It supports custom INI directives via -d flags, allowing quick setup of vulnerable configurations. Commonly used in offensive security for PoC environments targeting PHP flaws.

## Features

- Feature 1: Lightweight, no external dependencies
- Feature 2: Supports -d for runtime INI changes like disabling cleanup
- Feature 3: Handles HTTP/1.1 requests for multipart uploads

## Installation

### Requirements

- PHP 5.4+ installed

### Install Commands

```bash
# PHP is typically installed via package manager
sudo apt install php-cli  # On Ubuntu/Debian
```

## Basic Usage

```bash
php -S localhost:8000
```

### Common Options

| Option | Description |
|--------|-------------|
| `-S` | Start server on host:port |
| `-t` | Set document root |
| `-d` | Define INI setting |

## Examples

### Example 1: Basic Usage

```bash
php -S localhost:8000 -t /www/web/
```

### Example 2: Advanced Usage

```bash
php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on non-standard ports like 8000
- Process listings showing 'php -S' commands

## Related Procedures

- [[procedures/Setup-Vulnerable-PHP-Server]]

## Related Tools

- [[tools/Apache HTTP Server]]

## References

- Official documentation: https://www.php.net/manual/en/features.commandline.webserver.php
