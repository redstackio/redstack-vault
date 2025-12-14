---
id: tool-nmap
url: 'https://nmap.org/'
tags:
  - scanning
  - port-scan
  - recon
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.202Z'
validated: true
submitted: true
---
# nmap

**Status**: Verified

## Overview

Nmap (Network Mapper) is a free and open-source tool for network discovery and security auditing. In this context, it's used as a reference for the top 50 common TCP ports to guide SSRF-based scanning, helping prioritize tests for services like HTTP (80), SMB (445), and RDP (3389).

## Description

Nmap supports port scanning, service detection, and vulnerability scanning across hosts. For SSRF exploitation, attackers reference its --top-ports 50 output locally to select likely open ports on the target infrastructure, then replicate via URL parameters in requests. It's essential for reconnaissance in web exploitation scenarios where direct scanning is impossible.

## Features

- Feature 1: Port scanning with customizable top ports (e.g., --top-ports 50)
- Feature 2: Service version detection (-sV) for identifying protocols
- Feature 3: Scriptable scans with NSE for advanced recon

## Installation

### Requirements

- Standard Unix-like system or Windows with Npcap

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install nmap

# On macOS with Homebrew
brew install nmap

# On Windows: Download from nmap.org
```

## Basic Usage

```bash
nmap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--top-ports 50` | Scan top 50 common ports |
| `-p-` | Scan all 65535 ports |
| `-sV` | Detect service versions |

## Examples

### Example 1: Basic Usage

```bash
nmap --top-ports 50 localhost
```

> Scans localhost top 50 ports, outputting open ones like 80/tcp open http.

### Example 2: Advanced Usage

```bash
nmap -sV --top-ports 50 127.0.0.1
```

> Adds version detection for open ports.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing SYN scans on common ports
- Process monitoring for nmap executable
- IDS alerts on port scan patterns

## Related Procedures

- [[procedures/Exploit-SSRF-in-RelateIQ-Registration-for-Port-Scanning]]

## Related Tools

- [[tools/masscan]]
- [[tools/zmap]]

## References

- Official documentation: https://nmap.org/book/man.html
- Related resources: HackerOne Report #16571
