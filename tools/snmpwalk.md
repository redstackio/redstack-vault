---
type: tool
description: >-
  snmpwalk is a command-line tool that uses SNMP GETNEXT requests to query a
  network entity for a tree of information, typically related to the entity's
  management information base (MIB). It is commonly used for network
  reconnaissance and enumeration in security testing.
url: 'https://www.net-snmp.org/'
verified: true
platforms:
  - Linux
  - Windows
tags:
  - Enumeration
  - Network
commands:
  - '[[commands/snmpwalk-enumerate-server]]'
validated: true
---

# snmpwalk

**Status**: ✓ Verified

## Overview

snmpwalk is an SNMP application that performs a 'walk' of the Management Information Base (MIB) on a target device, retrieving a hierarchical dump of all accessible objects using repeated GETNEXT requests. It is widely used in offensive security for enumerating device details such as system information, interfaces, and configurations during reconnaissance phases.

## Description

snmpwalk queries SNMP-enabled devices to extract information from the MIB tree, starting from a specified OID (Object Identifier) or the root. It supports SNMP versions 1, 2c, and 3, allowing authenticated or unauthenticated access depending on the community string or credentials provided. In security testing, it helps map network devices, discover services, and gather sensitive data like hostnames, IP addresses, and running processes.

## Features

- Hierarchical MIB traversal using GETNEXT operations
- Support for SNMPv1, v2c, and v3 (with authentication and encryption)
- Output formatting options (e.g., numeric OIDs, environmental variables)
- Integration with MIB files for human-readable output
- Bulk request support for efficient querying

## Installation

### Requirements

- Standard C libraries and networking stack
- Optional: MIB files for readable output (via snmp-mibs-downloader)

### Install Commands

#### Debian/Ubuntu (Kali Linux)
```bash
sudo apt update
sudo apt install snmp
```

(Optional) For improved MIB readability:
```bash
sudo apt install snmp-mibs-downloader
sudo download-mibs
```

#### Windows

Download the Net-SNMP binaries from the official website (https://www.net-snmp.org/download.html) and install via the MSI package. Add the installation directory (e.g., C:\usr\bin) to your PATH environment variable.

#### macOS
```bash
brew install net-snmp
```

## Basic Usage

```bash
snmpwalk --help
```

This displays the help menu with all available options.

### Common Options

| Option | Description |
|--------|-------------|
| `-v VERSION` | Specify SNMP version (1, 2c, or 3) |
| `-c COMMUNITY` | Community string for authentication (v1/v2c) |
| `-O FORMAT` | Output format (e.g., 'e' for no OIDs, 'n' for numeric OIDs) |
| `-A AUTH_PASS` | Authentication password (v3) |
| `-X PRIV_PASS` | Privacy password (v3 with encryption) |
| `-l AUTH_PRIV` | Security level (noAuthNoPriv, authNoPriv, authPriv for v3) |

## Examples

### Example 1: Basic Usage

Enumerate a target using SNMPv1 with default community 'public':
```bash
snmpwalk -v 1 -c public 192.168.1.100
```

### Example 2: Advanced Usage

Perform a v2c walk with clean output (no OIDs) and timeout settings:
```bash
snmpwalk -v 2c -c private 10.10.10.10 -O e -t 5
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- Monitor UDP traffic on port 161 for SNMP queries from unauthorized sources
- Log SNMP authentication failures or unusual GETNEXT request volumes
- Enable SNMPv3 with strong authentication and encryption to mitigate v1/v2c risks
- Use network intrusion detection systems (NIDS) to alert on snmpwalk-like patterns

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/Nmap]]
- [[tools/snmpcheck]]

## References

- Official Net-SNMP Documentation: https://www.net-snmp.org/docs/man/snmpwalk.html
- SNMP Protocol Overview: https://datatracker.ietf.org/doc/html/rfc1157
