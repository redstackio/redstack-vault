---
type: tool
verified: true
created_at: '2019-08-28T21:17:29.431602+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - reconnaissance
  - scanning
url: 'https://www.si6networks.com/tools/ipv6toolkit/addr6'
validated: true
---

# addr6

**Status**: Unverified

## Overview

addr6 is an IPv6 address analysis and manipulation tool from the SI6 Networks' IPv6 Toolkit. It is designed for security assessments of IPv6 networks, allowing users to resolve hostnames to IPv6 addresses, generate candidate addresses from prefixes and patterns (such as MAC addresses), and perform address autoconfiguration analysis. Commonly used in reconnaissance phases to map and predict IPv6 address spaces.

## Description

The addr6 tool enables detailed manipulation and analysis of IPv6 addresses, supporting tasks like EUI-64 generation from MAC addresses, prefix-based address creation, and hostname resolution in IPv6 environments. It is part of a broader suite for IPv6 security testing, including attacks on Neighbor Discovery and fragmentation, but addr6 focuses specifically on address-related operations. It helps in troubleshooting IPv6 networking issues and assessing device resiliency against address-based attacks.

## Features

- Feature 1: Hostname to IPv6 address resolution for reconnaissance.
- Feature 2: Generation of IPv6 addresses from network prefixes and input patterns (e.g., MAC addresses).
- Feature 3: Support for IPv6 autoconfiguration analysis, including link-local and global address prediction.
- Feature 4: Integration with other toolkit tools like scan6 for comprehensive IPv6 scanning.

## Installation

### Requirements

- Linux system with IPv6 support enabled.
- Root privileges for some network-related operations.

### Install Commands

On Kali Linux or Ubuntu:

```bash
sudo apt update
sudo apt install ipv6-toolkit
```

On other distributions, compile from source:

```bash
wget https://www.si6networks.com/tools/ipv6toolkit/ipv6-toolkit-3.1.0.tar.gz
 tar -xzf ipv6-toolkit-3.1.0.tar.gz
 cd ipv6-toolkit-3.1.0
 ./configure
 make
 sudo make install
```

## Basic Usage

```bash
addr6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -p, --prefix | Specify IPv6 prefix for address generation |
| -m, --mac | Input MAC address for EUI-64 calculation |
| -r, --resolve | Resolve hostname to IPv6 addresses |

## Examples

### Example 1: Basic Usage

Resolve a hostname:

```bash
[[commands/addr6-resolve-hostname-to-ipv6]]
addr6 example.com
```

### Example 2: Advanced Usage

Generate addresses from prefix:

```bash
[[commands/addr6-generate-addresses-from-prefix]]
addr6 -p 2001:db8::/64 macs.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Network Service Scanning (for IPv6 address discovery)
- [[System Network Configuration Discovery]] System Network Configuration Discovery (IPv6 address analysis)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual IPv6 resolution queries or address generation patterns in network logs.
- Detection method 2: IPv6 traffic analysis showing prefix-based probing or EUI-64 derivations from known MACs.
- Detection method 3: Process monitoring for 'addr6' executions on endpoints.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scan6]] (IPv6 scanning companion tool)
- [[tools/Nmap]] (General network scanner with IPv6 support)

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/addr6
- IPv6 Toolkit GitHub: https://github.com/six-networks/ipv6-toolkit
- SI6 Networks' IPv6 Security Resources: https://www.si6networks.com/tools/ipv6toolkit/
