---
id: 17892c55-8d44-4952-bb1f-73adbe6d1a39
type: tool
verified: true
created_at: '2019-08-28T21:17:22.925210+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - snmp
  - reconnaissance
  - discovery
  - network-scanning
url: 'https://www.kali.org/tools/braa/'
validated: true
---

# braa

**Status**: Unverified

## Overview

Braa is a lightweight mass SNMP scanner designed for querying multiple hosts simultaneously in a single process. It is particularly useful in offensive security operations for rapid enumeration of SNMP-enabled devices on a network, such as discovering system information, interfaces, or other MIB data without the overhead of traditional SNMP tools like snmpwalk.

## Description

Braa implements a custom, minimal SNMP stack that supports basic data types (e.g., integers, strings, OIDs) but does not rely on external libraries like net-snmp. This makes it extremely fast for large-scale scans but limits it to non-standard, OID-based queries (numerical OIDs like .1.3.6.1.2.1.1.5.0 must be used instead of symbolic names). It excels in reconnaissance phases where speed is critical, allowing queries against dozens or hundreds of hosts with low resource consumption. Common use cases include network discovery, service enumeration, and collecting device details for further exploitation planning.

## Features

- **Mass Scanning**: Query multiple hosts in parallel within one process for efficiency.
- **Custom SNMP Implementation**: No external dependencies; supports SNMPv1/v2c communities.
- **Speed Optimized**: Minimal parsing (no ASN.1 support) for quick execution on large targets.
- **Basic Data Types**: Handles integers, strings, and OIDs; suitable for common MIB queries.
- **Timeout and Retry Options**: Configurable for unreliable networks.

## Installation

### Requirements

- Linux environment (tested on Debian-based distros like Kali Linux).
- Basic build tools if compiling from source (gcc, make).

### Install Commands

On Kali Linux, braa is pre-installed:

```bash
# Already available via /usr/bin/braa
braa --version
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install braa
```

From source (if needed):

```bash
wget http://www.pentestingschool.com/braa/braa-0.24.1.tar.gz
# Note: Source may be archived; check Kali repo for latest.
tar -xzf braa-0.24.1.tar.gz
cd braa-0.24.1
make
sudo make install
```

## Basic Usage

```bash
braa --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and exit |
| `-v` | Verbose output for debugging |
| `-t $_TIMEOUT` | Set timeout in seconds (default: 5) |
| `-r $_RETRIES` | Number of retries per query (default: 1) |
| `-s` | Use SNMPv1 (default is v2c) |

## Examples

### Example 1: Basic Usage

Query the system name (sysName) OID on a single host:

```bash
braa 192.168.1.1:public .1.3.6.1.2.1.1.5.0
```

### Example 2: Advanced Usage

Mass query sysDescr OID across multiple hosts with custom timeout:

```bash
braa -t 3 192.168.1.1:public 192.168.1.2:public 192.168.1.3:public .1.3.6.1.2.1.1.1.0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Discovery (SNMP enumeration for device and service details)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: Unusual SNMP queries (UDP port 161) from a single source to multiple targets in short bursts.
- Process monitoring: Execution of 'braa' binary with high CPU usage during scans.
- Logs: SNMP community string exposures or anomalous OID requests in SNMP traps/logs.
- IDS/IPS signatures: Patterns matching mass SNMP GET requests without standard library fingerprints.

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
- [[tools/Nmap]]

## References

- Kali Linux Tools: https://www.kali.org/tools/braa/
- Original Source: http://www.pentestingschool.com/braa/ (archived)
- GitHub Mirror: https://github.com/rapid7/metasploit-framework/tree/master (related modules)

*Last updated: 2023-10-01*
