---
url: 'https://www.php.net/manual/en/features.commandline.webserver.php'
tags:
  - web-server
  - testing
type: tool
verified: false
platforms:
  - Linux
  - Web
description: >-
  Simulates sequential request processing like a proxy for testing DoS impact in
  phpBB exploitation.
id: b0c65e05-8d7d-4702-a1a5-522a44be1f6d
created_at: '2025-12-14T17:26:49.082Z'
updated_at: '2025-12-14T17:26:49.082Z'
validated: true
submitted: true
---
# PHP-Built-in-HTTP-Server

**Status**: Unverified

## Overview

The PHP built-in development server is a lightweight HTTP server for testing PHP applications, used here to mimic proxy-like sequential processing to amplify DoS effects in vulnerability testing.

## Description

It handles PHP scripts without needing Apache or Nginx, ideal for local simulation of phpBB environments. In this context, it processes requests one-by-one, exacerbating hanging connections from path traversal.

## Features

- Feature 1: Runs PHP apps out-of-the-box
- Feature 2: Lightweight, no config needed
- Feature 3: Supports POST/multipart for upload simulations

## Installation

### Requirements

- PHP 5.4+ installed

### Install Commands

```bash
# No install needed if PHP is present
php -S 127.0.0.1:8082 -t /path/to/phpbb
```

## Basic Usage

```bash
php -S 127.0.0.1:8082
```

### Common Options

| Option | Description |
|--------|-------------|
| -S | Start server on host:port |
| -t | Document root directory |

## Examples

### Example 1: Basic Usage

```bash
php -S 127.0.0.1:8082 -t .
```

### Example 2: Advanced Usage

```bash
php -S 127.0.0.1:8082 -t /phpbb/dir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Process: php -S on non-standard ports
- Network: Localhost traffic on test ports like 8082

## Related Procedures


## Related Tools

- [[tools/nginx]]
- [[tools/Apache]]

## References

- Official documentation: https://www.php.net/manual/en/features.commandline.webserver.php
