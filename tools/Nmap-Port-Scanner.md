---
id: uuid-nmap-tool
url: 'https://nmap.org/'
tags:
  - recon
  - scanning
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.294Z'
validated: true
submitted: true
---
# Nmap-Port-Scanner

**Status**: Unverified

## Overview

Nmap is a free and open-source network mapper used for security auditing and reconnaissance, ideal for discovering open ports and services like exposed Solr instances.

## Description

Nmap supports various scan types including TCP SYN, UDP, and version detection. In offensive security, it's commonly used for initial host discovery and service enumeration to identify vulnerabilities in public-facing apps.

## Features

- Feature 1: Full port range scanning (-p-)
- Feature 2: Service version detection (-sV)
- Feature 3: OS fingerprinting (-O)

## Installation

### Requirements

- Linux/Windows/macOS
- Root/admin privileges for raw sockets

### Install Commands

```bash
# Ubuntu/Debian
apt update && apt install nmap

# Or download from nmap.org
```

## Basic Usage

```bash
nmap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Verbose output |
| -p- | All ports |

## Examples

### Example 1: Basic Usage

```bash
nmap target-ip
```

### Example 2: Advanced Usage

```bash
nmap -p- -T4 -sV target-ip
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: IDS signatures for SYN scan patterns
- Detection method 2: Log analysis for multiple connection attempts to ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Masscan]]
- [[tools/Zmap]]

## References

- Official documentation: https://nmap.org/book/man.html
- Related resources: Nmap scripting engine docs
