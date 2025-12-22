---
id: tool-gobuster
url: 'https://github.com/OJ/gobuster'
tags:
  - recon
  - bruteforce
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.534Z'
validated: true
submitted: true
---
# Gobuster

**Status**: Unverified

## Overview

Gobuster is a command-line tool for bruteforcing URIs (directories and files) on web servers, commonly used in penetration testing to discover hidden endpoints like unprotected admin directories.

## Description

Gobuster performs directory and file enumeration by sending HTTP requests against a target URL using a wordlist. It's fast, customizable, and supports extensions, making it ideal for identifying misconfigurations in web applications such as the DoD vuln where admin paths lack protection.

## Features

- Feature 1: Directory and file bruteforcing with wordlists
- Feature 2: Support for multiple extensions (e.g., php, html)
- Feature 3: Threading for speed and proxy integration

## Installation

### Requirements

- Go 1.11 or higher
- Git

### Install Commands

```bash
# Install via Go
GO111MODULE=on go install github.com/OJ/gobuster/v3@latest

# Or via package manager (e.g., Kali Linux)
apt update && apt install gobuster
```

## Basic Usage

```bash
gobuster dir --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target URL |
| `-w, --wordlist` | Path to wordlist |
| `-x, --extensions` | File extensions to append |
| `-t, --threads` | Number of threads |

## Examples

### Example 1: Basic Usage

```bash
gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt
```

### Example 2: Advanced Usage

```bash
gobuster dir -u https://target-dod-app.com/ -w directory-list-2.3-medium.txt -x php,html -t 50 --no-error
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of 404/403 responses from web server logs
- Unusual user-agent strings or rapid requests to /admin paths
- Network traffic spikes to common wordlist paths

## Related Procedures

- [[procedures/Directory-Bruteforcing-for-Unprotected-Endpoints]]

## Related Tools

- [[DirBuster]]
- [[ffuf]]

## References

- Official GitHub: https://github.com/OJ/gobuster
- OWASP Testing Guide
