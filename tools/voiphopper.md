---
id: af67038e-9ba9-40f1-904f-9fc6fea7ca2a
type: tool
verified: true
created_at: '2019-08-28T21:17:41.984500+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - voip
  - vlan-hopping
  - network
  - lateral-movement
  - revelation
url: 'https://sourceforge.net/projects/voiphopper/'
validated: true
---

# Voiphopper

**Status**: Unverified

## Overview

VoIP Hopper is a GPLv3 licensed security tool written in C that enables rapid VLAN hopping into the Voice VLAN on specific ethernet switches. It mimics the behavior of an IP Phone in environments such as Cisco, Avaya, Nortel, and Alcatel-Lucent, allowing testers to assess VoIP infrastructure security by gaining unauthorized access to segmented voice networks.

## Description

VoIP Hopper facilitates VLAN traversal for security testing by performing two key steps: discovering the 12-bit Voice VLAN ID (VVID) and creating a virtual VoIP ethernet interface to spoof traffic. It supports multiple discovery protocols including CDP (Cisco Discovery Protocol), DHCP, LLDP-MED (Link Layer Discovery Protocol - Media Endpoint Discovery), and 802.1q ARP. Once the VVID is identified, the tool inserts a spoofed 802.1q VLAN header into DHCP requests to obtain an IP address in the VoIP VLAN subnet. Subsequent ethernet frames are tagged with this header, effectively hopping into the voice network. This tool is primarily used in penetration testing to evaluate VLAN segmentation and VoIP security controls.

## Features

- VVID discovery via CDP, DHCP, LLDP-MED, and 802.1q ARP protocols
- Creation of a virtual VoIP ethernet interface on the operating system
- Spoofing of 802.1q VLAN headers in DHCP requests and subsequent traffic
- Support for Cisco, Avaya, Nortel, and Alcatel-Lucent switch environments
- Command-line interface for automated or manual VLAN hopping tests

## Installation

### Requirements

- Linux kernel with support for 802.1q VLAN tagging (most modern distributions)
- GCC compiler for building from source
- Root privileges for network interface manipulation
- Compatible ethernet interface (e.g., eth0)

### Install Commands

```bash
# Clone the repository from SourceForge or download the tarball
git clone https://git.code.sf.net/p/voiphopper/code voiphopper
cd voiphopper

# Compile the tool
make

# Install (optional, places binary in /usr/local/bin)
sudo make install
```

Alternatively, download pre-compiled binaries from the official SourceForge project page if available for your distribution.

## Basic Usage

```bash
voiphopper --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface` | Specify the ethernet interface (e.g., eth0) |
| `-d, --discover` | Discovery method: cdp, dhcp, lldp, arp |
| `-V, --vvid` | Manually specify the Voice VLAN ID (12-bit) |
| `-a, --auto` | Automatically discover VVID and perform hop |
| `-v, --verbose` | Enable verbose output for debugging |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Discover the VVID using CDP on interface eth0:

```bash
sudo voiphopper -i eth0 -d cdp
```

### Example 2: Advanced Usage

Perform automatic VLAN hop with verbose output:

```bash
sudo voiphopper -i eth0 -a -v
```

### Example 3: Manual Hop with Known VVID

Hop to a known Voice VLAN ID:

```bash
sudo voiphopper -i eth0 -V 100
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Cloud Instance Metadata API]] Unsecured Credentials: Credentials in Registry (adapted for network credential spoofing in VoIP contexts)
- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools (VLAN segmentation bypass)

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous CDP, LLDP-MED, or DHCP traffic from non-IP phone MAC addresses
- Unexpected 802.1q tagged frames on access ports
- Virtual interface creation (e.g., via `ip link` commands) on monitoring systems
- Network logs showing IP assignments in voice VLAN to unauthorized devices
- Switch logs for VLAN ID mismatches or spoofed phone behavior

## Related Commands

- [[commands/voiphopper-discover-vvid-cdp]]
- [[commands/voiphopper-discover-vvid-dhcp]]
- [[commands/voiphopper-perform-vlan-hop]]

## References

- Official project: https://sourceforge.net/projects/voiphopper/
- VoIP security testing guide: https://www.cisco.com/c/en/us/products/security/secure-access-control-system/index.html
- VLAN hopping techniques: OWASP or SANS Institute resources on network segmentation
