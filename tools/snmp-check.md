---
id: e935bb63-acaf-4b80-820f-e8d1f8f6920d
name: snmp-check
type: tool
verified: true
created_at: '2019-08-28T21:17:28.403145Z'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - Enumeration
  - Network
url: 'http://www.nothink.org/codes/snmpcheck/index.php'
commands:
  - '[[commands/snmp-check-host-enumeration]]'
validated: true
---

# snmp-check

**Status**: Unverified

## Overview

snmp-check is a tool for querying network entities via SNMP GETNEXT requests to retrieve a tree of information related to the entity. It formats results in a human-readable way, unlike snmpwalk which often requires additional processing. It is commonly used in offensive security for enumerating system details, network configurations, and services on SNMP-enabled devices during reconnaissance phases.

## Description

snmp-check enumerates various settings on SNMP-enabled targets, providing structured output on aspects such as system information, network interfaces, processes, and more. It supports SNMP versions 1, 2c, and 3, and can detect write access separately. Key enumeration areas include contact details, device descriptions, domain information, hardware and storage, hostname, IIS statistics, IP forwarding, listening UDP ports, location, MOTD, mount points, network interfaces, services, processes, routing, software components, system uptime, TCP connections, total memory, and user accounts. This makes it valuable for discovery in network penetration testing.

## Features

- Human-friendly formatted SNMP enumeration output
- Support for SNMPv1, v2c, and v3
- Detection of write access to SNMP objects
- Comprehensive coverage of system, network, and process information
- No additional add-ons required for readable results

## Installation

### Requirements

- Perl (snmp-check is a Perl script)
- Net-SNMP library or equivalent SNMP support

### Install Commands

For Debian/Ubuntu (note: existing documentation mentions Ruby, but snmp-check is Perl-based; adjust as needed):

```bash
# Install Perl and SNMP dependencies
sudo apt update
sudo apt install perl libnet-snmp-perl

# Download snmp-check
wget http://www.nothink.org/codes/snmpcheck/snmp-check-1.9.pl -O snmp-check
chmod +x snmp-check
sudo mv snmp-check /usr/local/bin/
```

For Windows:

- Install ActivePerl or Strawberry Perl
- Download the script from the official site and place it in a directory in your PATH
- Ensure SNMP libraries are available via CPAN if needed

## Basic Usage

```bash
snmp-check --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c <community>` | Specify SNMP community string |
| `-v <version>` | SNMP version (1, 2c, 3) |
| `-t <timeout>` | Connection timeout in seconds |
| `-r <retries>` | Number of retries |

## Examples

### Example 1: Basic Usage

Enumerate a host using SNMPv2c with public community:

```bash
snmp-check -c public -v 2c 10.10.10.10
```

### Example 2: Advanced Usage

Enumerate with custom timeout:

```bash
snmp-check -c private -v 1 192.168.1.100 -t 2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Information Discovery]] System Information Discovery
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to UDP port 161 (SNMP) from reconnaissance tools
- SNMP queries with common community strings like 'public' or 'private'
- Log entries for SNMP GETNEXT requests in network monitoring tools
- Presence of snmp-check binary or script on compromised hosts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/snmpwalk]]
- [[tools/onesixtyone]]

## References

- Official website: http://www.nothink.org/codes/snmpcheck/index.php
- Source code and documentation from the author
