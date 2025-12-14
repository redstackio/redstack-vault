---
id: tool-php
url: 'https://www.php.net/'
tags:
  - scripting
  - server-side
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.036Z'
validated: true
submitted: true
---
# PHP

**Status**: Unverified

## Overview

Server-side scripting language for web development, used here to host dynamic content that logs cookies and executes cURL requests.

## Description

PHP processes incoming HTTP requests on the taken-over subdomain, accessing $_SERVER['HTTP_COOKIE'] and integrating with cURL for backend calls.

## Features

- Feature 1: Server-side execution
- Feature 2: Access to HTTP headers
- Feature 3: Integration with cURL

## Installation

### Requirements

- Web server (Apache)

### Install Commands

```bash
apt install php libapache2-mod-php
```

## Basic Usage

```bash
php --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -S | Start built-in server |

## Examples

### Example 1: Basic Usage

```bash
php -S localhost:8000
```

### Example 2: Advanced Usage

Embed in HTML/PHP files for request handling

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Python (adapted for PHP)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- PHP error logs
- Anomalous script executions

## Related Procedures

- [[procedures/Host-Malicious-Content-on-Taken-Over-Subdomain]]

## Related Tools


## References

- php.net manual
