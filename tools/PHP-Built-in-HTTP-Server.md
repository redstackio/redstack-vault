---
url: 'https://www.php.net/manual/en/features.commandline.webserver.php'
tags:
  - web-server
  - testing
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.070Z'
id: e9e52526-4adf-4153-a08f-30ed515f31fe
validated: true
submitted: true
---
---

# PHP-Built-in-HTTP-Server

**Status**: Unverified

## Overview

PHP's built-in development server for simulating web environments, used here to test sequential request processing for DoS impacts behind proxies.

## Description

The tool runs a lightweight HTTP server via CLI, ideal for local phpBB testing. It processes requests sequentially, mimicking proxy behavior to demonstrate hanging connections from path traversal.

## Features

- Feature 1: Simple startup with php -S
- Feature 2: Supports PHP scripts like phpBB
- Feature 3: No external dependencies

## Installation

### Requirements

- PHP 7+ installed

### Install Commands

```bash
# No installation needed if PHP is present
php -v  # Verify
```

## Basic Usage

```bash
php -S 127.0.0.1:8082 -t /path/to/phpbb/
```

### Common Options

| Option | Description |
|--------|-------------|
| -S | Address:port to bind |
| -t | Document root |

## Examples

### Example 1: Basic Usage

```bash
php -S 127.0.0.1:8082
```

### Example 2: Advanced Usage

```bash
php -S 127.0.0.1:8082 /path/to/phpbb/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: php -S on non-standard ports
- Network: Localhost bindings

## Related Procedures


## Related Tools

- [[nginx]]
- [[Apache]]

## References

- Official PHP docs

