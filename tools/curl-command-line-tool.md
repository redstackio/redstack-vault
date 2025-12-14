---
url: 'https://curl.se/'
tags:
  - transfer
  - http
  - rce
type: tool
platforms:
  - Linux
  - POSIX
  - Windows
  - macOS
description: >-
  Command-line tool for transferring data with URLs, vulnerable to RCE via
  --engine arbitrary library loading.
id: de9e9e79-207b-4134-a874-f726e81f3cea
created_at: '2025-12-14T17:23:31.180Z'
updated_at: '2025-12-14T17:23:31.180Z'
verified: false
validated: true
submitted: true
---
# curl-command-line-tool

**Status**: Unverified

## Overview

curl is a versatile command-line client for URLs, supporting numerous protocols. In security testing, it's exploited for RCE via --engine on POSIX systems by loading malicious .so files.

## Description

curl transfers data using protocols like HTTP, HTTPS, FTP. The --engine option loads custom SSL engines as shared libraries without validation, enabling constructor-based code execution. Common in scripts, CI/CD, and web backends.

## Features

- Feature 1: Supports HTTPS with OpenSSL
- Feature 2: --engine for custom crypto engines
- Feature 3: Verbose output for debugging

## Installation

### Requirements

- POSIX-like OS
- OpenSSL libraries

### Install Commands

```bash
# On Ubuntu/Debian
apt install curl

# Or build from source
wget https://curl.se/download/curl-8.13.0.tar.gz && tar -xzf curl-8.13.0.tar.gz && cd curl-8.13.0 && ./configure && make && make install
```

## Basic Usage

```bash
curl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-V, --version` | Show version info |
| `--engine` | Use SSL engine |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
curl https://example.com
```

### Example 2: Advanced Usage

```bash
curl --engine evil_engine.so https://example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Dynamic Linker Hijacking]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for curl with --engine arguments
- Audit logs of .so library loads during curl execution

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[wget]]
- [[httpie]]

## References

- Official documentation: https://curl.se/docs/manpage.html
- Related resources: HackerOne Report #3293801
