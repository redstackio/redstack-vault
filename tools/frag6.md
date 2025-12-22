---
id: 4b883af6-4373-4d6e-bf40-2436982af777
type: tool
verified: true
created_at: '2019-08-28T21:17:38.356908+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - fragmentation
  - network-attack
  - assessment
url: 'https://www.si6networks.com/tools/ipv6toolkit/'
validated: true
---

# frag6

**Status**: Unverified

## Overview

frag6 is a specialized tool from the SI6 Networks' IPv6 Toolkit designed for performing IPv6 fragmentation-based attacks and security assessments. It allows testers to craft and send fragmented IPv6 packets to evaluate how devices handle fragmentation, identify vulnerabilities in reassembly processes, and simulate attacks like overlapping fragments or atomic fragment exploits.

## Description

The tool supports sending arbitrary fragmented IPv6 packets, testing for issues such as improper reassembly, buffer overflows, or bypasses of security filters. It is particularly useful in IPv6 network penetration testing, red team exercises targeting IPv6-enabled devices, and troubleshooting fragmentation-related problems. frag6 operates at the network layer, requiring raw socket access, and is command-line driven for precise control over packet parameters.

## Features

- Fragmentation attack simulation (overlapping, out-of-order fragments)
- Assessment of IPv6 reassembly mechanisms
- Support for various protocols (TCP, UDP, ICMPv6)
- Customizable fragment offsets, lengths, and identification
- Integration with other IPv6 Toolkit tools for comprehensive testing

## Installation

### Requirements

- Linux kernel with IPv6 support
- Root privileges for raw socket access
- libnetfilter-queue and libpcap development libraries

### Install Commands

```bash
# Clone the IPv6 Toolkit repository
git clone https://github.com/six2dez/sixtools.git
cd sixtools/src

# Compile (requires autoconf, automake, etc.)
./autogen.sh
./configure
make
sudo make install

# Alternative: Install via package manager if available (e.g., on Debian-based)
sudo apt update
sudo apt install ipv6toolkit
```

## Basic Usage

```bash
frag6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output |
| -s <src> | Specify source IPv6 address |
| -d <dst> | Specify destination IPv6 address |
| -i <if> | Network interface |
| -p <proto> | Protocol (tcp, udp, icmp6) |

## Examples

### Example 1: Basic Usage

Send a basic fragmented packet:

```bash
frag6 -s 2001:db8::1 -d 2001:db8::2 -p tcp -i eth0
```

### Example 2: Advanced Usage

Test overlapping fragments:

```bash
frag6 -s 2001:db8::1 -d 2001:db8::2 -p icmp6 -o -f 0 -l 1280 -i eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (for fragmentation DoS)
- [[Archive Collected Data]] Archive Collected Data (if used in evasion)

### Tactics

- [[Impact]] Impact
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IPv6 fragmented traffic patterns (e.g., high volume of fragments with same ID)
- Network logs showing raw IPv6 packet crafting from assessment tools
- Process monitoring for frag6 execution (e.g., via sysdig or auditd)
- IDS/IPS alerts on anomalous fragmentation (e.g., Snort rules for IPv6 frag attacks)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scan6]] (IPv6 scanning)
- [[tools/ra6]] (Router Advertisement attacks)

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/frag6.shtml
- GitHub repository: https://github.com/six2dez/sixtools
- IPv6 Security Best Practices: RFC 7112
