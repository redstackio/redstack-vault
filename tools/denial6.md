---
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - exploitation
  - dos
  - packet-crafting
url: 'https://github.com/fgervais/denial6'
validated: true
---

# denial6

**Status**: Unverified

## Overview

Denial6 is a comprehensive toolkit designed to exploit vulnerabilities in IPv6 and ICMPv6 protocols. It includes modules for performing denial-of-service attacks, spoofing, and other manipulations, along with a packet factory library for custom packet creation. Commonly used in red teaming for network reconnaissance and disruption in IPv6 environments.

Category: Exploitation

## Description

The tool targets inherent weaknesses in IPv6 protocols such as Router Advertisements (RA), Neighbor Discovery (ND), and ICMPv6 messages. It leverages Scapy for packet manipulation and supports various attack vectors like flooding, spoofing, and redirection. Ideal for testing IPv6 network security, simulating attacks, or educational purposes in controlled environments.

Supported Platforms: Linux (requires Python 3 and Scapy)

## Features

- RA and ND flooding for DoS
- Spoofing of IPv6 control messages
- Custom packet factory for ICMPv6 and IPv6 payloads
- Integration with network interfaces for live attacks
- Offline packet generation for analysis

## Installation

### Requirements

- Python 3.6+
- Scapy library
- Root privileges for packet injection

### Install Commands

```bash
# On Kali/Ubuntu
sudo apt update
sudo apt install python3-pip git
pip3 install scapy

# Clone and install denial6
git clone https://github.com/fgervais/denial6.git
cd denial6
sudo python3 setup.py install
```

For macOS or Windows, use virtual environments and ensure Npcap/WinPcap for packet capture.

## Basic Usage

```bash
python3 -m denial6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface |
| -v, --verbose | Enable verbose output |
| --help | Show module help |

## Examples

### Example 1: Basic Usage

View available modules:

```bash
python3 -m denial6 --list-modules
```

### Example 2: Advanced Usage

Run an RA flood (see related command for details):

```bash
python3 -m denial6 ra flood --interface eth0 --target ff02::1
```

## Related Commands

- [[commands/denial6-ra-flood]]
- [[commands/denial6-nd-spoof]]
- [[commands/denial6-packet-factory-create]]

## References

- Official GitHub: https://github.com/fgervais/denial6
- Scapy Documentation: https://scapy.net
