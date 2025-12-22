---
id: d88eb6a4-b979-4c56-bebe-f3e6b0224857
type: tool
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reconnaissance
  - discovery
  - ident-protocol
  - user-enumeration
url: 'https://github.com/strainp/ident-user-enum'
validated: true
---

# ident-user-enum

**Status**: Unverified

## Overview

ident-user-enum is a Perl script designed for enumerating user accounts on remote systems by querying the Ident service (port 113/TCP). It helps identify the owners of processes listening on specific TCP ports, allowing pentesters to prioritize high-privilege services (e.g., those running as root) for further attacks. The gathered usernames can also support password guessing on other services.

## Description

The tool connects to the Ident service on a target host and queries it for each specified port to retrieve the username associated with the listening process. This is particularly useful in reconnaissance phases to map service ownership without direct access. It supports batch processing of port lists and handles timeouts for unreliable networks. Commonly used in Unix/Linux environments where Ident is enabled, though many modern systems disable it for security reasons.

## Features

- Queries Ident (RFC 1413) protocol for user information per port
- Supports single targets or IP ranges
- Handles port lists from files for efficient scanning
- Verbose output for debugging connections
- Timeout configuration to avoid hanging on unresponsive hosts

## Installation

### Requirements

- Perl 5 (with Socket module, usually included)
- Network access to target port 113/TCP

### Install Commands

```bash
# Download the script from GitHub
wget https://raw.githubusercontent.com/strainp/ident-user-enum/master/ident-user-enum.pl -O ident-user-enum.pl

# Make it executable
chmod +x ident-user-enum.pl

# Or clone the repo if available
# git clone https://github.com/strainp/ident-user-enum.git
```

On Kali Linux, it may be available via package managers or custom repos, but manual download is recommended for the latest version.

## Basic Usage

```bash
./ident-user-enum.pl <target> <port>
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v` | Verbose mode for detailed connection info |
| `-t <timeout>` | Set connection timeout in seconds (default: 5) |
| `-f <portfile>` | Read ports from a file instead of command-line |

## Examples

### Example 1: Basic Usage

Scan a single port on a target:

```bash
./ident-user-enum.pl 192.168.1.100 80
```

### Example 2: Advanced Usage

Enumerate users for multiple ports from a file with timeout:

```bash
./ident-user-enum.pl -f ports.txt -t 10 192.168.1.100
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound connections to port 113/TCP from scanning hosts
- Perl process spawning with network socket activity
- Log entries for Ident queries in target system auth logs (e.g., /var/log/auth.log)
- Network IDS alerts on unusual Ident protocol traffic

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
- [[tools/masscan]]

## References

- Official GitHub: https://github.com/strainp/ident-user-enum
- RFC 1413 (Ident Protocol): https://datatracker.ietf.org/doc/html/rfc1413
