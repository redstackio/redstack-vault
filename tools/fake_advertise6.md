---
id: c61dfe4d-371c-4708-805f-bde0e9b5ad0f
type: tool
verified: true
created_at: '2019-08-28T21:17:22.907059+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - spoofing
  - router-advertisement
  - network-attack
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# fake_advertise6

**Status**: Unverified

## Overview

fake_advertise6 is a specialized tool from the THC-IPv6 toolkit designed to send forged IPv6 Router Advertisement (RA) messages. It exploits weaknesses in the IPv6 Neighbor Discovery Protocol (NDP) to perform attacks such as router spoofing, prefix delegation manipulation, and traffic redirection, commonly used in red team exercises to demonstrate IPv6 network vulnerabilities.

## Description

This tool generates and transmits fake ICMPv6 Router Advertisement packets over a specified network interface. It supports various options to customize the RA, including adding prefixes, routes, DNS servers, and MTU settings. In offensive security operations, it's typically used to intercept traffic by becoming the default router for IPv6 hosts or to cause denial-of-service by advertising invalid configurations. The tool is part of a broader suite for testing IPv6 protocol security, highlighting issues like lack of authentication in RA messages.

## Features

- Feature 1: Send basic RA messages to spoof router presence
- Feature 2: Include custom prefixes for address autoconfiguration attacks
- Feature 3: Advertise routes, DNS resolvers, and MTU to manipulate host behavior
- Feature 4: Support for multiple RA types (e.g., with ARO, RDNSS options)

## Installation

### Requirements

- Linux kernel with IPv6 support
- Root privileges for raw socket access
- THC-IPv6 toolkit dependencies (libnetfilter-queue, libpcap)

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install thc-ipv6

# Manual build from source
sudo apt install libnetfilter-queue-dev libpcap-dev libpthread-stubs0-dev
wget https://github.com/vanhauser-thc/thc-ipv6/archive/master.zip
unzip master.zip
cd thc-ipv6-master
./configure && make && sudo make install
```

## Basic Usage

```bash
fake_advertise6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -A | Include Address Registration Option (ARO) |
| -D | Include DNS server information |
| -P prefix/len | Advertise a specific prefix |
| -R | Include Route Information Option |
| -S | Send solicited RA |

## Examples

### Example 1: Basic Usage

Send a simple fake RA on interface eth0.

```bash
sudo fake_advertise6 eth0
```

### Example 2: Advanced Usage

Advertise a custom prefix and DNS server.

```bash
sudo fake_advertise6 eth0 -P 2001:db8::/64 -D 2001:db8::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for traffic redirection via spoofed RAs)
- [[Direct Network Flood]] Network Denial of Service: IPv6 Neighbor Discovery Manipulation

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unexpected ICMPv6 RA packets (Type 134) with anomalous router lifetimes or prefixes using tools like tcpdump or Wireshark
- Detection method 2: Enable RA Guard on switches/routers (RFC 7113) to filter unauthorized RAs
- Detection method 3: Log IPv6 NDP traffic and alert on multiple RAs from the same link-local address

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[thc-ipv6-toolkit]]
- [[scapy]] (for custom IPv6 packet crafting)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in the toolkit man pages
- IPv6 Security Considerations: RFC 7113 (RA Guard)
