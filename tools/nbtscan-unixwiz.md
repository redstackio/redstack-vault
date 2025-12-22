---
type: tool
description: >-
  Command-line tool for scanning NETBIOS nameservers on local or remote TCP/IP
  networks to discover Windows hosts and potential open shares.
url: 'http://www.unixwiz.net/tools/nbtscan.html'
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
  - macOS
tags:
  - reconnaissance
  - netbios
  - network-discovery
  - windows-enumeration
validated: true
---

# nbtscan-unixwiz

**Status**: Unverified

## Overview

nbtscan-unixwiz is a lightweight command-line tool designed for network reconnaissance, specifically targeting NETBIOS (NetBIOS over TCP/IP) services. It scans IP ranges to identify Windows hosts broadcasting NETBIOS names, providing information on hostnames, workgroups/domains, and MAC addresses. This tool is particularly useful in the initial phases of penetration testing to map Windows environments and locate potential file shares without requiring authentication.

## Description

Similar to the Windows nbtstat utility but extended to operate on entire subnets or IP ranges, nbtscan-unixwiz sends NETBIOS name queries to discover active hosts. It can reveal node types (e.g., workstation, server), registered names, and basic system details, making it a foundational tool for SMB enumeration and lateral movement planning in Active Directory environments. The tool supports various output formats and options for filtering results, enhancing its utility in automated scripts or red team operations.

## Features

- Feature 1: Scans single IPs, ranges, or CIDR notations for NETBIOS responses.
- Feature 2: Retrieves detailed node status including OS hints, workgroup/domain names, and MAC addresses.
- Feature 3: Supports custom separators, output redirection, and reverse lookups for comprehensive enumeration.
- Feature 4: Lightweight and fast, with no dependencies on GUI or heavy libraries.

## Installation

### Requirements

- Unix-like system (Linux, macOS, BSD).
- Standard build tools (gcc, make).
- No additional runtime dependencies.

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros, but to build from source):
apt update && apt install build-essential

# Download and compile from source (unixwiz version):
wget http://www.unixwiz.net/tools/nbtscan-1.5.1.tar.gz
tar -xzf nbtscan-1.5.1.tar.gz
cd nbtscan-1.5.1
./configure
make
sudo make install

# On Ubuntu/Debian:
apt install nbtscan

# On macOS (using Homebrew):
brew install nbtscan
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
| -m | Query machine status for detailed info (OS, workgroup). |
| -R | Perform reverse NETBIOS name lookup. |
| -s SEP | Set output separator (default tab). |
| -l | List names only, no status. |

## Examples

### Example 1: Basic Usage

Scan a local subnet for NETBIOS hosts:

```bash
nbtscan 192.168.1.0/24
```

### Example 2: Advanced Usage

Scan with machine status and output to file:

```bash
nbtscan -m -s ' ' 10.0.0.1-10.0.0.254 > netbios_enum.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Remote System Discovery]] Remote System Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic showing UDP port 137 queries (NETBIOS Name Service) from scanning IPs.
- Detection method 2: IDS/IPS alerts for anomalous NETBIOS broadcasts or sweeps on internal networks.
- Detection method 3: Process monitoring for 'nbtscan' executions in logs (e.g., via Sysmon or auditd).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Tool: nmap]]
- [[Tool: enum4linux]]

## References

- Official website: http://www.unixwiz.net/tools/nbtscan.html
- Man page: man nbtscan
- Related resource: MITRE ATT&CK for Enterprise

## Related Commands

- [[commands/nbtscan-basic-network-scan]]
- [[commands/nbtscan-scan-with-machine-status]]
- [[commands/nbtscan-resolve-names]]
