---
id: 9cabd917-1751-4218-b077-393ef97bd7f1
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - exploitation
  - network-attack
  - packet-crafting
url: ''
commands:
  - '[[commands/fake-router6-send-rogue-router-advertisement]]'
  - '[[commands/fake-router6-neighbor-discovery-spoof]]'
  - '[[commands/fake-router6-create-icmpv6-packet]]'
validated: true
---

# fake-router6

**Status**: Unverified

## Overview

fake-router6 is a specialized toolset for exploiting weaknesses in IPv6 and ICMPv6 protocols. It enables security researchers and red teams to perform attacks such as router advertisement spoofing, neighbor discovery manipulation, and custom packet injection. The tool includes a packet factory library that simplifies the creation of malicious IPv6 packets for testing protocol robustness and simulating real-world attacks.

## Description

This tool targets inherent vulnerabilities in IPv6 implementations, including issues with Router Advertisements (RA), Neighbor Discovery Protocol (NDP), and ICMPv6 messages. It is particularly useful in network penetration testing to demonstrate risks like unauthorized route injection, address spoofing, and denial-of-service via packet floods. The integrated packet factory library allows for programmatic packet construction using Python, making it extensible for custom exploits. Common use cases include IPv6 reconnaissance, man-in-the-middle attacks, and protocol fuzzing in lab environments.

## Features

- **Rogue RA Generation**: Craft and send fake router advertisements to redirect traffic or install malicious default gateways.
- **NDP Spoofing**: Spoof neighbor advertisements to poison ARP-like caches in IPv6 networks.
- **ICMPv6 Manipulation**: Generate custom ICMPv6 packets for error simulation, neighbor solicitation, and DoS attacks.
- **Packet Factory Library**: Python-based API for building and dissecting IPv6 packets without external dependencies like Scapy.
- **Interface Support**: Works on multiple network interfaces with verbose logging for debugging.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- Python 3.6+.
- Root privileges for raw socket access (e.g., via sudo).
- libpcap-dev for packet capture (optional, for monitoring).

### Install Commands

```bash
# Clone the repository (assuming open-source availability)
git clone https://github.com/example/fake-router6.git
cd fake-router6

# Install dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x fake_router6.py
```

On Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
sudo ./fake_router6.py --help
```

This displays available subcommands like 'send-ra', 'nd-spoof', and 'packet-factory'.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-i, --interface` | Specify the network interface (e.g., eth0) |
| `-v, --verbose` | Enable detailed logging of sent/received packets |
| `-t, --target` | IPv6 target address or prefix |
| `--dry-run` | Simulate packet sending without transmission |

## Examples

### Example 1: Basic Rogue RA Attack

Use the dedicated command for sending rogue router advertisements:

See [[commands/fake-router6-send-rogue-router-advertisement]] for full details.

### Example 2: Neighbor Discovery Spoofing

Spoof NDP messages to impersonate a neighbor:

See [[commands/fake-router6-neighbor-discovery-spoof]] for full details.

### Example 3: Custom ICMPv6 Packet Creation

Leverage the packet factory to build and send a custom packet:

See [[commands/fake-router6-create-icmpv6-packet]] for full details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Reflection Amplification]] Service Stop (for IPv6 DoS via ICMP floods)
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and Relay (extended to NDP spoofing in IPv6)
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (packet crafting for exfiltration simulation)

### Tactics

- [[Defense Evasion]] Defense Evasion (protocol manipulation to bypass IPv4-focused defenses)
- [[Impact]] Impact (DoS through IPv6 protocol abuse)
- [[Privilege Escalation]] Privilege Escalation (via route hijacking for lateral movement)

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous ICMPv6 traffic volumes, especially Router Advertisements from unauthorized sources.
- Mismatched source IPs in NDP messages (use tools like tcpdump: `tcpdump -i eth0 ip6 and icmp6`).
- Unexpected default gateway changes on hosts (monitor with `ip -6 route`).
- Packet captures showing non-standard IPv6 options or malformed ICMPv6 payloads.
- Process monitoring for python scripts with raw socket binds on IPv6 interfaces.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scapy]] (complementary packet crafting library)
- [[tools/thc-ipv6]] (similar IPv6 attack toolkit)
- [[tools/Nmap]] (for IPv6 host discovery prior to attacks)

## References

- RFC 4861: Neighbor Discovery for IP version 6
- RFC 4862: IPv6 Stateless Address Autoconfiguration
- Official GitHub repository (if available) or security research papers on IPv6 attacks
