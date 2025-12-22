---
id: c873e10b-f0f6-411e-93da-9340e377a988
type: tool
description: >-
  A tool from the THC-IPv6 toolkit designed to exploit weaknesses in IPv6 and
  ICMPv6 protocols by performing fake DNS updates, enabling attacks like DNS
  cache poisoning and record injection.
verified: true
url: 'https://github.com/vanhauser-thc/thc-ipv6'
tags:
  - ipv6
  - dns
  - exploitation
  - network-attack
platforms:
  - Linux
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
validated: true
---

# fake-dnsupdate6

**Status**: Unverified

## Overview

fake_dnsupdate6 is a specialized tool from the THC-IPv6 toolkit used to attack inherent protocol weaknesses in IPv6 and ICMPv6. It allows for the injection of fake DNS updates, which can lead to DNS cache poisoning, redirection of traffic, or disruption of IPv6 network services. Commonly used in penetration testing to demonstrate IPv6-specific vulnerabilities in DNS resolution processes.

## Description

This tool exploits the lack of strong authentication in some IPv6 DNS update mechanisms by crafting and sending unauthorized DNS update packets. It includes an easy-to-use packet factory library for generating custom IPv6 and ICMPv6 packets. In offensive security operations, it's typically employed during network exploitation phases to manipulate DNS records, enabling further attacks like man-in-the-middle or denial-of-service in IPv6 environments. The tool requires IPv6 connectivity and is most effective against networks with misconfigured or legacy DNS servers supporting dynamic updates.

## Features

- Fake DNS record addition/deletion/prerequisite checks over IPv6
- Custom packet crafting for IPv6 and ICMPv6 protocols
- Support for zone transfers and dynamic update simulations
- Integrated library for building complex packet sequences
- Verbose logging for debugging attack payloads

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Root privileges for raw socket access
- Dependencies: libnetfilter-queue, libpcap (usually handled by the toolkit installer)

### Install Commands

On Kali Linux (pre-installed as part of thc-ipv6):
```bash
# Already available, verify with:
which fake_dnsupdate6
```

For Ubuntu/Debian:
```bash
sudo apt update
sudo apt install thc-ipv6
```

For manual compilation from source:
```bash
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6
./configure
make
sudo make install
```

## Basic Usage

```bash
fake_dnsupdate6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --domain | Specify the target domain for DNS updates |
| -A, --add | Add a new DNS record (e.g., AAAA for IPv6) |
| -D, --delete | Delete an existing DNS record |
| -P, --prerequisite | Check prerequisites before update |
| -z, --zone | Specify the DNS zone |
| -v, --verbose | Enable verbose output for debugging |
| -6, --ipv6 | Force IPv6 mode (default) |

## Examples

### Example 1: Basic Usage - Add a Fake AAAA Record

Add a fake IPv6 address record for a domain:
```bash
fake_dnsupdate6 -d example.com -A 2001:db8::1
```

This sends a DNS update packet to the authoritative server for example.com, attempting to add an AAAA record pointing to the attacker's IPv6 address.

### Example 2: Advanced Usage - Delete Record with Prerequisite Check

First check if a record exists, then delete it:
```bash
fake_dnsupdate6 -d example.com -P "name example.com AAAA" -D 2001:db8::1
```

This verifies the existence of the record before attempting deletion, useful for targeted manipulations.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Reflection Amplification]] Service Stop (for disrupting DNS services via invalid updates)
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and Relay (extended to IPv6 DNS contexts)
- [[Standard Application Layer Protocol]] Application Layer Protocol (abusing DNS over IPv6)

### Tactics

- [[Impact]] Impact (disruption of network services)
- [[Persistence]] Persistence (via persistent DNS record manipulation)
- [[Resource Development]] Resource Development (tooling for network attacks)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IPv6 UDP traffic on port 53 (DNS) from non-authoritative sources
- Anomalous DNS update packets in network captures (e.g., via Wireshark filters for DNS Update opcode)
- Log entries in DNS servers for rejected or suspicious dynamic updates
- Increased ICMPv6 error messages related to invalid DNS payloads
- Process monitoring for thc-ipv6 binaries on compromised hosts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/thc-ipv6-toolkit]]
- [[tools/scapy]] (for custom IPv6 packet crafting)
- [[tools/Nmap]] (for IPv6 reconnaissance)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Toolkit Documentation: https://www.thc.org/thc-ipv6/
- IPv6 Security Considerations: RFC 4940
