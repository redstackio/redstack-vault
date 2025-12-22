---
id: 7fbe838c-e560-45d8-a50a-b4ca0244d9e4
type: tool
verified: true
description: >-
  SNMP community string brute forcer for enumerating and testing SNMPv1/v2c
  services
url: 'https://github.com/trapkit/onesixtyone'
platforms:
  - Linux
  - Windows
tags:
  - Brute Force
  - Network
category: Reconnaissance
created_at: '2020-02-19T04:34:40.056998+00:00'
updated_at: '2023-05-30T19:58:27.277347+00:00'
validated: true
---

# onesixtyone

**Status**: ✓ Verified

## Overview

onesixtyone is a fast SNMP scanner designed for brute-forcing SNMPv1 and SNMPv2c community strings. It sends parallel SNMP GET requests to a target host or network range, testing multiple community strings from a dictionary file until a valid one is found or all are exhausted. This tool is commonly used in reconnaissance to enumerate SNMP services, extract system information, and identify weak or default community strings like 'public' or 'private'.

## Description

onesixtyone operates by performing asynchronous SNMP queries, making it efficient for large wordlists and multiple targets. When a valid community string is discovered, it retrieves basic MIB information such as system description, contact, location, and other OIDs. It supports targeting single IPs, hostnames, or CIDR subnets. The tool does not support SNMPv3 and focuses on community string discovery rather than full MIB walking (use tools like snmpwalk for deeper enumeration after success).

## Features

- Dictionary-based brute forcing of community strings
- Support for single hosts, multiple IPs, or CIDR ranges (e.g., 192.168.1.0/24)
- Multi-threaded parallel requests for speed
- Basic OID enumeration on successful communities (e.g., sysDescr, sysContact)
- Verbose output for monitoring progress and results
- Lightweight and easy to integrate into scripts or penetration testing workflows

## Installation

### Requirements

- C compiler (gcc) for source builds
- libpcap-dev on Linux for network features

### Install Commands

#### Debian/Ubuntu/Kali

```bash
sudo apt update
sudo apt install onesixtyone
```

#### Windows

Download precompiled binaries from the GitHub releases or compile using MinGW:

```bash
# Using MSYS2 or similar
pacman -S mingw-w64-x86_64-gcc
# Clone and build from source
git clone https://github.com/trapkit/onesixtyone.git
cd onesixtyone
make
```

#### From Source (All Platforms)

```bash
git clone https://github.com/trapkit/onesixtyone.git
cd onesixtyone
make
sudo make install
```

## Basic Usage

```bash
onesixtyone --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c FILE` | Specify file containing community strings (one per line) |
| `-w` | Enable wordlist mode (default behavior with -c) |
| `-v` | Verbose output showing all attempts |
| `-C COMMUNITY` | Test a single community string |
| `-i INTERFACE` | Bind to specific network interface |
| `-O` | Output format (default is human-readable) |

## Examples

### Example 1: Basic Usage

Brute force community strings on a single target using a common wordlist:

```bash
onesixtyone -c /usr/share/wordlists/snmp.txt 192.168.1.100
```

### Example 2: Advanced Usage

Scan a subnet with verbose output:

```bash
onesixtyone -v -c communities.txt 192.168.1.0/24
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

- Network traffic: High volume of UDP/161 SNMP GET requests from a single source to multiple targets
- SNMP logs on targets showing repeated invalid community attempts
- Process monitoring: Execution of 'onesixtyone' binary with dictionary files
- IDS/IPS rules for SNMP brute force patterns (e.g., Snort rules for UDP/161 floods)

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
- [[Metasploit]]
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/trapkit/onesixtyone
- Original Author: Michel Arboi (http://www.nothink.org/onesixtyone/)
- SNMP Enumeration Guide: https://www.offsec.com/metasploit-unleashed/snmp/
