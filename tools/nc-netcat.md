---
id: tool-nc-netcat
url: 'https://nc110.sourceforge.net/'
tags:
  - networking
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.064Z'
validated: true
submitted: true
---
# nc-netcat

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking tool for reading/writing data across TCP/UDP connections, commonly used in security testing for sending raw HTTP requests and payloads.

## Description

In this attack, nc delivers crafted SSRF HTTP requests to the target port 80, enabling minimal payloads without a full HTTP client.

## Features

- Feature 1: Raw TCP/UDP socket manipulation
- Feature 2: Port scanning and banner grabbing
- Feature 3: Data piping for scripted attacks

## Installation

### Requirements

- Standard Unix-like system

### Install Commands

```bash
# On Debian/Ubuntu
apt install netcat
# On macOS
brew install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -v | Verbose output |
| -n | No DNS resolution |
| -w 3 | Timeout in seconds |

## Examples

### Example 1: Basic Usage

```bash
nc target-ip 80
```

### Example 2: Advanced Usage

```bash
echo "GET / HTTP/1.1\r\n\r\n" | nc target-ip 80
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Execution]] Execution
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing raw TCP connections to port 80
- Unusual echo/netcat processes in process lists

## Related Procedures

- [[procedures/Trigger-SSRF-with-Crafted-HTTP-Request]]
- [[procedures/Port-Scan-Internal-Services-via-XSPA]]

## Related Tools

- [[tools/curl]]
- [[tools/nmap]]

## References

- Official documentation: https://nc110.sourceforge.net/
- Related resources: Netcat man pages
