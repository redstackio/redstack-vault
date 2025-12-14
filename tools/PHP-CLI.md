---
id: tool-php-cli
name: PHP-CLI
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.750Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - php
  - cli
url: 'https://www.php.net/manual/en/features.commandline.php'
validated: true
submitted: true
---

# PHP-CLI

**Status**: Unverified

## Overview

PHP Command Line Interface (CLI) is the built-in tool for executing PHP scripts from the terminal, essential for generating cryptographic payloads in exploits like Vaultpress signature bypass.

## Description

PHP CLI allows running server-side scripts locally, including those using OpenSSL for key generation and signing. In offensive security, it's used for crafting exploit payloads without a web server.

## Features

- Feature 1: Direct execution of PHP files with extensions like OpenSSL
- Feature 2: No web server required for script testing
- Feature 3: Supports complex crypto operations for PoCs

## Installation

### Requirements

- Operating system with package manager (apt, brew, etc.)
- OpenSSL library

### Install Commands

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install php-cli php-openssl

# macOS
brew install php

# Windows: Download from php.net
```

## Basic Usage

```bash
php --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v` | Display PHP version |

## Examples

### Example 1: Basic Usage

```bash
php script.php
```

### Example 2: Advanced Usage

```bash
php -d extension=openssl genkey.php
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] Command and Scripting Interpreter (PHP)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor process lists for php.exe or php binary executions
- Log file accesses to custom PHP scripts in temp directories
- Alert on OpenSSL function calls in non-web contexts

## Related Procedures


## Related Tools

- [[tools/Curl]]

## References

- Official documentation: https://www.php.net/manual/en/features.commandline.php
- OpenSSL in PHP: https://www.php.net/manual/en/book.openssl.php
