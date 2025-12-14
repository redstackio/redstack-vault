---
id: tool-php-fsockopen-001
url: 'https://www.php.net/manual/en/function.fsockopen.php'
tags:
  - php
  - socket
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:09.911Z'
validated: true
submitted: true
---
# fsockopen

**Status**: Unverified

## Overview

fsockopen is a PHP function for opening socket connections to send raw HTTP requests, useful in PoCs for crafting custom packets without external tools like curl.

## Description

It enables low-level network interactions in PHP scripts, ideal for exploiting web vulnerabilities by sending malformed requests directly to TCP ports.

## Features

- Feature 1: Opens internet or Unix sockets
- Feature 2: Supports timeout and error handling
- Feature 3: Integrates with fwrite/fread for request/response

## Installation

### Requirements

- PHP with sockets extension (default)

### Install Commands

```bash
# Enabled by default in PHP
php -m | grep sockets
```

## Basic Usage

```php
$fp = fsockopen('localhost', 80);
```

### Common Options

| Option | Description |
|--------|-------------|
| `hostname` | Target host |
| `port` | Target port |
| `timeout` | Connection timeout in seconds |

## Examples

### Example 1: Basic Usage

```php
$fp = fsockopen('localhost', 8000, $errno, $errstr, 30);
if (!$fp) { echo "Error: $errstr ($errno)"; }
```

### Example 2: Advanced Usage

```php
$fp = fsockopen('localhost', 8000);
fwrite($fp, $http_request);
$response = fread($fp, 1024);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- PHP scripts with fsockopen calls in logs
- Unusual socket connections from web processes

## Related Procedures

- [[procedures/Prepare-Malformed-Multipart-Request-PoC]]

## Related Tools

- [[tools/curl]]

## References

- Official documentation: https://www.php.net/manual/en/function.fsockopen.php
