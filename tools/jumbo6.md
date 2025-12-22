---
id: 81aa68e3-57f4-4ffb-96ba-78509f019eb7
type: tool
verified: true
created_at: '2019-08-28T21:17:21.638713Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - jumbogram
  - network-testing
  - denial-of-service
url: 'https://www.si6networks.com/tools/ipv6-toolkit/'
commands:
  - '[[commands/jumbo6-send-basic-jumbogram]]'
  - '[[commands/jumbo6-flood-with-jumbograms]]'
  - '[[commands/jumbo6-test-fragmentation-handling]]'
validated: true
---

# jumbo6

**Status**: Unverified

## Overview

jumbo6 is a specialized tool from the SI6 Networks' IPv6 Toolkit designed to assess potential flaws in the handling of IPv6 Jumbograms. It crafts and sends IPv6 packets with the Jumbo Payload option to test target systems' IPv6 stack implementations for vulnerabilities, such as denial-of-service conditions or improper processing of large payloads.

## Description

IPv6 Jumbograms allow transmission of payloads larger than 65,535 bytes, but many implementations handle them poorly, leading to crashes or resource exhaustion. jumbo6 enables security researchers to send crafted jumbograms, fragmented or unfragmented, to evaluate device resiliency. It is part of a broader IPv6 security assessment suite but focuses specifically on jumbo payload issues. Common use cases include penetration testing of IPv6-enabled networks, vulnerability research, and troubleshooting IPv6 protocol stacks.

## Features

- Feature 1: Craft arbitrary IPv6 jumbograms with customizable payload sizes
- Feature 2: Support for fragmentation of jumbograms to test reassembly logic
- Feature 3: Flooding capabilities to simulate DoS attacks via oversized packets
- Feature 4: Spoofed source IP addressing for anonymous testing
- Feature 5: Verbose logging for packet details and transmission status

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- libpcap development libraries (for packet crafting)
- GCC compiler
- Git

### Install Commands

The jumbo6 tool is part of the IPv6 Toolkit. Install the full toolkit:

```bash
# Clone the repository
sudo git clone https://github.com/fgont/ipv6-toolkit.git
cd ipv6-toolkit

# Compile and install
sudo make
sudo make install
```

On Kali Linux, it may be available via apt:

```bash
sudo apt update
sudo apt install ipv6-toolkit
```

Verify installation:

```bash
jumbo6 --help
```

## Basic Usage

```bash
jumbo6 --help
```

This displays available options, such as -d for destination, --jumbo for payload size, and -c for packet count.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| -d <ip> | Specify destination IPv6 address |
| -s <ip> | Specify source IPv6 address |
| --jumbo <size> | Set jumbo payload size |
| -c <count> | Send multiple packets |
| --frag | Enable fragmentation |

## Examples

### Example 1: Basic Usage

Send a single jumbogram:

```bash
jumbo6 -d 2001:db8::1 -s 2001:db8::2 --jumbo 65536
```

### Example 2: Advanced Usage

Flood with fragmented jumbograms:

```bash
jumbo6 -d 2001:db8::1 --jumbo 100000 --frag -c 100 -i 0.5
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual IPv6 traffic with Jumbo Payload option enabled (using tools like tcpdump: `tcpdump -i eth0 ip6 and 'ip6[6] == 94'`)
- Detection method 2: High volume of oversized IPv6 packets causing resource spikes on IPv6-enabled interfaces
- Detection method 3: Log analysis for spoofed source IPs in IPv6 traffic
- Detection method 4: Network IDS signatures for jumbogram floods (e.g., Snort rules for IPv6 extension headers)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/addr6]]
- [[tools/frag6]]
- [[tools/scan6]]

## References

- Official documentation: https://www.si6networks.com/tools/ipv6-toolkit/jumbo6
- GitHub Repository: https://github.com/fgont/ipv6-toolkit
- IPv6 Jumbograms RFC: https://datatracker.ietf.org/doc/html/rfc2675
