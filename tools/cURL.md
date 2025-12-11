---
url: 'https://curl.se/'
tags:
  - http
  - authentication
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Command-line tool for transferring data with URLs.
id: 8d2b3ffb-b039-4438-bb83-9385bfcbdeeb
created_at: '2025-12-11T03:48:06.073Z'
updated_at: '2025-12-11T03:48:06.073Z'
verified: false
validated: true
submitted: true
---
# curl

**Status**: Unverified

## Overview

Curl is a command-line client for making HTTP requests, commonly used in security testing for API interactions and authentication testing.

## Description

Curl supports various protocols and authentication methods, including client certificates, making it suitable for exploiting leaked credentials.

## Features

- HTTP requests: GET, POST, etc.
- Authentication: Basic, cert-based
- Custom headers and data

## Installation

### Requirements

- Compatible OS

### Install Commands

```bash
sudo apt install curl  # Debian-based
```

## Basic Usage

```bash
curl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-u, --user` | Specify user and password |
| `--cert` | Client certificate file |

## Examples

### Example 1: Basic Usage

```bash
curl https://example.com
```

### Example 2: Advanced Usage

```bash
curl -u user: --cert cert.pem https://api.example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor HTTP traffic for curl user-agents
- Log authentication attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #git

## References

- https://curl.se/docs
