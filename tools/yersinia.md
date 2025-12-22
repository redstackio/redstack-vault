---
id: 371435d1-eb44-4a3f-8d0c-9a749c0f4047
type: tool
verified: true
created_at: '2019-08-28T21:17:21.959127+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - layer2
  - protocol-attack
  - stp
  - cdp
  - dhcp
url: 'http://yersinia.sourceforge.net/'
validated: true
---

# Yersinia

**Status**: Unverified

## Overview

Yersinia is a comprehensive framework designed for layer 2 network attacks, exploiting vulnerabilities in various Ethernet and wireless protocols. It is primarily used in penetration testing and red team operations to assess the resilience of network infrastructure against protocol-specific weaknesses, such as spanning tree manipulation or DHCP spoofing.

## Description

Yersinia provides a structured environment for launching attacks on layer 2 protocols, simulating real-world threats like network disruptions, unauthorized access, or denial-of-service conditions. It supports both console and GUI modes for flexibility in different testing scenarios. The tool is particularly valuable for auditing switches, routers, and wireless access points in enterprise networks. Supported protocols include Spanning Tree Protocol (STP) for loop prevention attacks, Cisco Discovery Protocol (CDP) for device enumeration and manipulation, Dynamic Trunking Protocol (DTP) for trunking exploits, Dynamic Host Configuration Protocol (DHCP) for IP assignment interference, Hot Standby Router Protocol (HSRP) for gateway redundancy attacks, 802.1q for VLAN tagging issues, 802.1x for authentication bypass, Inter-Switch Link Protocol (ISL) for legacy trunking, and VLAN Trunking Protocol (VTP) for configuration propagation vulnerabilities.

## Features

- **Protocol Support**: Attacks on STP, CDP, DTP, DHCP, HSRP, 802.1q, 802.1x, ISL, VTP.
- **Modes**: Interactive console (-C), GUI (-G), and interface-specific launches.
- **Attack Types**: Configuration manipulation, denial-of-service, sniffing, and packet injection.
- **Cross-Platform Interface Selection**: Works with Ethernet, wireless, and virtual interfaces.
- **Logging and Counters**: Tracks attack progress and packet statistics.

## Installation

### Requirements

- Linux kernel with packet capture support (libpcap).
- Root privileges for raw socket access.
- Network interface in promiscuous mode capability.

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install yersinia

# On Ubuntu/Debian
sudo apt update && sudo apt install yersinia

# On Fedora/CentOS
sudo dnf install yersinia  # or yum install yersinia

# From Source (if needed)
# Download from http://yersinia.sourceforge.net/
# ./configure && make && sudo make install
```

## Basic Usage

```bash
yersinia --help
```

This displays available options, including modes and protocols. Always run as root (sudo) for interface access.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --version | Display version information |
| -I, --dev <interface> | Select network interface (e.g., eth0) |
| -G | Launch in GUI mode |
| -C | Launch in console mode |
| -i | Interactive mode (default) |

## Examples

### Example 1: Basic Usage

```bash
sudo yersinia -I eth0
```

Selects eth0 and enters interactive mode to choose protocols and attacks.

### Example 2: Advanced Usage

```bash
sudo yersinia -C -I wlan0
```

Launches console mode on a wireless interface for testing 802.1x or DHCP attacks.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools
- [[Network Service Scanning]] Network Service Discovery

### Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual raw packet traffic on layer 2 (e.g., excessive STP BPDUs via Wireshark).
- Process monitoring for 'yersinia' binary running as root.
- Network logs showing protocol anomalies like rogue DHCP offers or VTP updates.
- Interface promiscuous mode enabled without authorization.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ettercap]]
- [[tools/Scapy]]

## References

- Official website: http://yersinia.sourceforge.net/
- SourceForge repository: https://sourceforge.net/projects/yersinia/
- Man page: man yersinia
