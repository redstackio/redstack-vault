---
url: 'https://www.php.net/manual/en/features.commandline.webserver.php'
tags:
  - hosting
  - development-server
  - php
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Lightweight HTTP server included with PHP for development and quick file
  serving.
id: acdd9110-9494-44fc-bc66-7f4fbd9d94dd
created_at: '2025-12-14T04:08:55.323Z'
updated_at: '2025-12-14T04:08:55.323Z'
verified: false
validated: true
submitted: true
---
# PHP-Built-in-Server

**Status**: Unverified

## Overview

The PHP Built-in Server is a simple, command-line HTTP server bundled with PHP, ideal for quickly hosting static files and PHP scripts during security testing, such as SSRF exploitation setups.

## Description

It supports serving files from a directory, executing PHP code, and binding to specific addresses/ports. In offensive security, it's used to host PoC files like redirection scripts without needing Apache or Nginx. Common in quick prototypes for attacks involving external fetches.

## Features

- Feature 1: Serves static HTML/JS and dynamic PHP
- Feature 2: Binds to IPv4/IPv6 interfaces
- Feature 3: Lightweight, no configuration files needed

## Installation

### Requirements

- PHP 5.4+ installed

### Install Commands

```bash
# PHP is typically installed via package manager
sudo apt install php-cli  # Ubuntu/Debian
```

## Basic Usage

```bash
php -S localhost:8000
```

### Common Options

| Option | Description |
|--------|-------------|
| `-S` | Server mode |
| `-t` | Document root directory |
| `-h` | Help message |

## Examples

### Example 1: Basic Usage

```bash
php -S 0.0.0.0:80
```

### Example 2: Advanced Usage

```bash
php -S 0.0.0.0:80 -t ./attack-files
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'php -S' executions
- Network logs showing development server ports (e.g., 80 from non-standard IPs)

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://www.php.net/manual/en/features.commandline.webserver.php
