---
type: tool
description: >-
  A tool for flooding DHCPv6 servers by sending rapid DHCP discover messages,
  exploiting IPv6 protocol weaknesses to cause denial of service or IP
  exhaustion.
url: 'https://github.com/vanhauser-thc/thc-ipv6'
tags:
  - ipv6
  - dhcpv6
  - dos
  - flooding
  - exploitation
platforms:
  - Linux
verified: true
validated: true
---

# flood_dhcpc6

**Status**: Unverified

## Overview

flood_dhcpc6 is part of the THC-IPv6 toolkit, designed to attack inherent weaknesses in IPv6 and ICMPv6 protocols. It specifically targets DHCPv6 by flooding servers with discover messages, leading to resource exhaustion, denial of service, or unauthorized IP allocation. Commonly used in penetration testing for network resilience assessment against IPv6-specific attacks.

## Description

This tool generates and sends a high volume of DHCPv6 solicitation (discover) packets from a specified interface, simulating multiple clients requesting IP addresses. It can overwhelm DHCPv6 servers, causing them to deplete lease pools or crash under load. The toolkit also includes a packet factory library for custom IPv6 packet crafting, enabling advanced protocol manipulation.

## Features

- Feature 1: Rapid DHCPv6 discover packet generation and transmission
- Feature 2: Support for custom packet crafting via included library
- Feature 3: Verbose logging for monitoring flood progress
- Feature 4: Integration with other THC-IPv6 tools for chained attacks

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Root privileges for raw socket access
- THC-IPv6 toolkit dependencies (libnetfilter-queue, etc.)

### Install Commands

```bash
# On Kali Linux (pre-installed or via apt)
apt update && apt install thc-ipv6

# From source
apt install git build-essential libnetfilter-queue-dev libpcap-dev
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6
./configure
make
sudo make install
```

## Basic Usage

```bash
flood_dhcpc6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the network interface |
| -v, --verbose | Enable verbose output |
| -c, --count | Limit the number of packets to send |

## Examples

### Example 1: Basic Usage

```bash
sudo flood_dhcpc6 -i eth0
```

Floods the DHCPv6 server on eth0 interface until stopped.

### Example 2: Advanced Usage

```bash
sudo flood_dhcpc6 -v -c 10000 -i eth0
```

Sends 10,000 packets verbosely on eth0.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Data Manipulation]] Data Manipulation (via protocol flooding)

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Sudden spike in DHCPv6 discover packets from a single source MAC/IP
- Detection method 2: Server logs showing lease exhaustion or high request volume
- Detection method 3: Network monitoring tools (e.g., Wireshark) capturing anomalous IPv6 traffic on UDP port 547
- Detection method 4: Process monitoring for flood_dhcpc6 binary or THC-IPv6 toolkit processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[thc-ipv6]]
- [[scapy]]

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in the repository README
- IPv6 Security Considerations: RFC 7113
