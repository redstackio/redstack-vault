---
id: tool-uuid-001
url: 'https://nmap.org/'
tags:
  - scanning
  - recon
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Network
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.653Z'
validated: true
submitted: true
---
# nmap

**Status**: Unverified

## Overview

Nmap is a network scanning tool used for host discovery, port scanning, and service enumeration in security testing.

## Description

Nmap supports advanced scripting via NSE for detailed service interrogation, such as SMB security checks. Commonly used in offensive operations for initial reconnaissance.

## Features

- Feature 1: Port scanning with version detection
- Feature 2: Scriptable vulnerability scanning
- Feature 3: Output in multiple formats (XML, grepable)

## Installation

### Requirements

- Linux/Windows/macOS with network privileges

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install nmap

# On macOS with Homebrew
brew install nmap
```

## Basic Usage

```bash
nmap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Specify ports |
| `--script` | Run NSE scripts |
| `-oN` | Normal output to file |

## Examples

### Example 1: Basic Usage

```bash
nmap -p 445 192.168.1.1
```

### Example 2: Advanced Usage

```bash
nmap -p 445 --script smb-security-mode 192.168.1.0/24
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing SYN scans on port 445
- IDS alerts for NSE script execution

## Related Procedures

- [[procedures/Discover-Exposed-SMB-Servers]]

## Related Tools

- [[tools/smbclient]]

## References

- Official documentation: https://nmap.org/book/man.html
