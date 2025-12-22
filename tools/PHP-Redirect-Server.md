---
id: t2b2c3d4-e5f6-7890-abcd-ef1234567896
url: 'https://www.php.net/manual/en/function.header.php'
tags:
  - php
  - redirect
  - server
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:09.973Z'
validated: true
submitted: true
---
# PHP Redirect Server

**Status**: Unverified

## Overview

PHP scripts serve as a simple redirect server to perform open redirects with custom HTTP status codes, used in exploits to chain requests across domains like in Flash upload bypasses.

## Description

A basic PHP file using header() function creates an open redirect endpoint. In security testing, it's configured to accept parameters for target URL and status (e.g., 307), forwarding requests without validation. Commonly hosted on Apache/Nginx with PHP module.

## Features

- Feature 1: Customizable redirect status codes (301, 307, 308)
- Feature 2: Parameter-based target selection
- Feature 3: Lightweight, no external dependencies

## Installation

### Requirements

- PHP 5+ installed
- Web server (Apache, Nginx)

### Install Commands

```bash
# Install PHP on Ubuntu
sudo apt update && sudo apt install php libapache2-mod-php
# Or for Nginx: sudo apt install php-fpm
sudo systemctl restart apache2
```

## Basic Usage

```bash
php -S localhost:8000  # For built-in server
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A (script-based) | Use in PHP code |

## Examples

### Example 1: Basic Usage

Create redirect.php:

```php
<?php
header('Location: ' . $_GET['target'], true, 307);
?>
```
Access: http://localhost/redirect.php?target=https://example.com

### Example 2: Advanced Usage

With status param:

```php
<?php
$status = $_GET['status'] ?? 307;
$target = $_GET['input'];
header("Location: $target", true, $status);
?>
```
Access: http://localhost/redirect.php?input=https://plus.google.com&status=308

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- HTTP logs showing 3xx redirects with dynamic parameters
- PHP files with header() calls to external domains

## Related Procedures


## Related Tools

- [[tools/ActionScript-Compiler]]

## References

- Official documentation: https://www.php.net/manual/en/function.header.php
- Related resources: PHP security guides
