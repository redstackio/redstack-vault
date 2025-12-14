---
url: 'https://github.com/ffuf/ffuf'
tags:
  - fuzzing
  - web
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.917Z'
id: f7d6dc97-b74d-4497-8c3f-5fdbd1bd85a1
validated: true
submitted: true
---
# ffuf

**Status**: Unverified

## Overview

Web fuzzer for directories, parameters, and virtual host discovery.

## Description

Ffuf is used for brute-forcing web paths, headers, and chained exploits like SSRF fuzzing in this attack.

## Features

- Feature 1: Multi-protocol support
- Feature 2: Custom headers
- Feature 3: Filtering options

## Installation

### Requirements

- Go 1.13+

### Install Commands

```bash
go install github.com/ffuf/ffuf@latest
```

## Basic Usage

```bash
ffuf -w wordlist -u target/FUZZ
```

### Common Options

| Option | Description |
|--------|-------------|
| `-w` | Wordlist |
| `-u` | URL |
| `-H` | Header |

## Examples

### Example 1: Basic Usage

```bash
ffuf -w common.txt -u https://app/FUZZ
```

### Example 2: Advanced Usage

```bash
ffuf -w payloads.txt -H "Cookie: FUZZ" -u target
```

## MITRE ATT&CK Mapping

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- High volume HTTP requests
- 404/200 pattern anomalies

## Related Procedures

- [[procedures/Enumerate-Subdomains-and-Expose-Git-Repository]]
- [[procedures/Exploit-SSRF-and-Open-Redirect-to-Discover-APK]]

## Related Tools

- [[tools/gobuster]]

## References

- GitHub documentation
