---
type: tool
verified: true
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - network
  - netbios
  - reconnaissance
url: 'http://www.tatiana.cmc.msu.ru/software/nbtscan/'
validated: true
---

# nbtscan

**Status**: ✓ Verified

## Overview

nbtscan is a command-line tool for scanning networks to discover NetBIOS name information from Windows and other systems supporting NetBIOS over TCP/IP. It sends NetBIOS status queries to IP addresses in a specified range, identifying active hosts, their computer names, logged-in users, and MAC addresses. Commonly used in penetration testing for initial network reconnaissance to map Windows environments.

## Description

nbtscan operates by mimicking NetBIOS name service queries (UDP port 137) and node status requests (UDP port 137 or 138). It processes responses to enumerate details without requiring authentication, making it effective for discovering legacy Windows systems, domain-joined machines, and potential entry points in Active Directory environments. The tool is lightweight, fast for small to medium subnets, and outputs results in a tabular format for easy parsing.

## Features

- Feature 1: Scans IP ranges in CIDR notation for efficient subnet coverage.
- Feature 2: Extracts NetBIOS names, usernames, server types, and MAC addresses from responses.
- Feature 3: Handles errors gracefully, reporting permission denials or timeouts for non-responsive hosts.
- Feature 4: Supports output redirection for scripting and integration with other tools like grep or awk.

## Installation

### Requirements

- Standard C libraries (glibc on Linux).
- Administrative privileges not required for scanning, but firewall rules may need adjustment for UDP traffic.

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install nbtscan

# On Windows
# Download binary from official site or compile from source using MinGW
# Source: http://www.tatiana.cmc.msu.ru/software/nbtscan/

# From source (Linux/Windows)
git clone https://github.com/openwall/nbtscan.git
cd nbtscan
make
sudo make install
```

## Basic Usage

```bash
nbtscan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage. |
| -v, --version | Display version information. |
| -r | Scan in reverse mode (hostnames to IPs, less common). |
| -S | Use TCP instead of UDP for queries (for firewalls blocking UDP). |
| -o file | Output results to a file. |

## Examples

### Example 1: Basic Usage

Scan a /24 subnet for NetBIOS hosts:

```bash
nbtscan 10.10.10.0/24
```

### Example 2: Advanced Usage

Scan with output to file and TCP mode:

```bash
nbtscan -S -o netbios_scan.txt 192.168.1.0/24
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Remote System Discovery]] Remote System Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual UDP traffic to port 137/138 from scanning tools (e.g., via network IDS like Snort rules for NetBIOS queries).
- Detection method 2: Log anomalous outbound NetBIOS requests from non-Windows systems or unexpected IPs.
- Detection method 3: Endpoint detection of nbtscan process or its signatures in process lists.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/enum4linux]]

## References

- Official documentation: http://www.tatiana.cmc.msu.ru/software/nbtscan/
- GitHub mirror: https://github.com/resurrecting-open-source-projects/nbtscan
- Related resources: MITRE ATT&CK for T1046
