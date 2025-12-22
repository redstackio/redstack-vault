---
id: ed3dde79-7a8e-4a74-9fcb-e538521d2c81
type: tool
verified: true
created_at: '2019-08-28T21:17:29.085072+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Network
tags:
  - snmp
  - cisco
  - reconnaissance
  - config-extraction
url: ''
validated: true
---

# copy-router-config

**Status**: Unverified

## Overview

copy-router-config is a Perl-based tool designed to extract configuration files from Cisco network devices that support SNMP (Simple Network Management Protocol). It is commonly used in penetration testing and network reconnaissance to retrieve sensitive configuration data, such as access credentials, routing tables, and device settings, without direct console access. This tool is particularly useful for auditing network infrastructure or identifying misconfigurations in environments with SNMP enabled.

## Description

The tool leverages SNMP to query and download the running configuration from Cisco routers and switches. It supports SNMPv1, v2c, and potentially v3, allowing testers to target devices where community strings are weak or default. Once extracted, the config files can reveal valuable information like SNMP communities, enable passwords (often in cleartext or weakly hashed), interface configurations, and ACLs. It is part of the Kali Linux distribution's SNMP toolkit and is invoked as a command-line script.

## Features

- SNMP-based configuration retrieval from Cisco IOS devices
- Support for multiple SNMP versions (v1/v2c primary)
- Output to file for offline analysis
- Option to specify custom MIB files for extended querying
- Verbose logging for troubleshooting SNMP interactions

## Installation

### Requirements

- Perl 5.x with SNMP modules (Net::SNMP)
- Access to a network with SNMP-enabled Cisco devices
- Root or sufficient privileges for network scanning (if needed)

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install copy-router-config

# Manual installation from source (if available)
# Clone or download from Kali tools repo
git clone https://gitlab.com/kalilinux/packages/copy-router-config.git
cd copy-router-config
sudo make install
```

## Basic Usage

```bash
copy-router-config --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage |
| `-H, --host` | Target Cisco device IP or hostname |
| `-C, --community` | SNMP community string (default: public) |
| `-v, --version` | SNMP version (1 or 2) |
| `-f, --file` | MIB file for custom OIDs (optional) |
| `-o, --output` | Output file for the configuration |
| `-V, --verbose` | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

Extract the running configuration from a Cisco router using the default community string:

```bash
copy-router-config -H 192.168.1.1 -C public -o router_config.txt
```

This queries the device at 192.168.1.1 and saves the config to router_config.txt.

### Example 2: Advanced Usage

Extract config with SNMPv2, verbose output, and custom MIB:

```bash
copy-router-config -H router.example.com -C private -v 2 -f custom.mib -o advanced_config.txt -V
```

This uses SNMPv2c, a custom MIB file, and provides detailed logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for SNMP enumeration)
- [[System Information Discovery]] System Information Discovery (via config extraction)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- SNMP traffic spikes to Cisco devices with unusual GET requests for config OIDs (e.g., 1.3.6.1.4.1.9.9.96)
- Log entries in Cisco devices for SNMP authentication failures or successful queries from unknown sources
- Network monitoring tools (e.g., Wireshark) capturing SNMP packets with community strings
- File creation on attacker systems with router config content (search for .txt or .cfg files with Cisco syntax)

## Related Commands

- [[commands/copy-router-config-extract-config]]

## Related Tools

- [[tools/snmpcheck]]
- [[tools/onesixtyone]]

## References

- Kali Linux Tools: https://www.kali.org/tools/copy-router-config/
- Cisco SNMP Configuration Guide: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-16-9/snmp-xe-16-9-book.html
