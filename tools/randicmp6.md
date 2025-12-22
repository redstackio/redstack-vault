---
id: 05046696-fbdb-4930-aa50-8eace5a7ef4e
type: tool
verified: true
created_at: '2019-08-28T21:17:24.985577+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - exploitation
  - reconnaissance
url: 'https://github.com/vitlabuda/randicmp6'
validated: true
---

# randicmp6

**Status**: Unverified

## Overview

Randicmp6 is a specialized toolset for exploiting weaknesses in the IPv6 and ICMPv6 protocols. It provides capabilities for crafting and sending customized ICMPv6 packets, including support for attacks like router advertisement spoofing, neighbor discovery manipulation, and denial-of-service floods. The tool includes a packet factory library for easy integration into custom scripts, making it ideal for red team operations targeting IPv6-enabled networks.

## Description

Randicmp6 targets inherent vulnerabilities in IPv6 implementations, such as lack of authentication in Neighbor Discovery Protocol (NDP) and Router Advertisements. It allows security testers to simulate real-world attacks, including redirecting traffic, poisoning caches, or overwhelming targets with malformed packets. Written in Rust, it offers high performance and reliability for packet generation and transmission. Common use cases include network reconnaissance, protocol testing, and offensive security assessments in IPv6 environments.

## Features

- **Packet Factory Library**: Easy-to-use API for building custom ICMPv6 packets programmatically.
- **Spoofing Support**: Craft packets with arbitrary source IPs and MAC addresses.
- **Attack Modes**: Built-in support for RA spoofing, NS/NA floods, and redirect attacks.
- **Randomization**: Options to randomize packet fields for evasion and testing variability.
- **Interface Binding**: Specify network interfaces for targeted transmission.
- **Verbose Logging**: Detailed output for debugging and analysis.

## Installation

### Requirements

- Rust toolchain (cargo and rustc, version 1.50 or later)
- Root privileges for raw socket access
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone the repository
 git clone https://github.com/vitlabuda/randicmp6.git
 cd randicmp6

# Build and install
 cargo build --release
 sudo cp target/release/randicmp6 /usr/local/bin/

# Or install directly via cargo (if available in crates.io)
 cargo install randicmp6
```

For Kali Linux or Ubuntu:

```bash
# Install Rust if not present
 curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
 source $HOME/.cargo/env

# Then follow the clone and build steps above
```

## Basic Usage

```bash
randicmp6 --help
```

This displays all available subcommands (e.g., ra for Router Advertisement, ns for Neighbor Solicitation) and global options like --interface and --verbose.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --verbose | Enable verbose packet logging |
| --interface <IFACE> | Bind to specific network interface |
| --source-ip <IP> | Spoof source IPv6 address |

## Examples

### Example 1: Basic Usage

Send a simple Router Advertisement:

```bash
sudo randicmp6 ra --interface eth0 --target-prefix 2001:db8::/64
```

### Example 2: Advanced Usage

Flood with Neighbor Solicitations:

```bash
sudo randicmp6 ns --flood --count 500 --target 2001:db8::1 --interface eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Network Denial of Service]] Network Denial of Service (for flood attacks)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for spoofing and redirects)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Monitoring**: Anomalous ICMPv6 traffic volumes or types (e.g., excessive RAs from non-router IPs) via tools like Wireshark or tcpdump.
- **Host Logs**: Kernel logs showing unexpected NDP cache updates or interface errors.
- **Process Monitoring**: Presence of randicmp6 binary or high raw socket usage by unknown processes.
- **IDS/IPS Signatures**: Alerts for spoofed ICMPv6 packets or NDP protocol abuse (e.g., Snort rules for IPv6 floods).
- **Endpoint Detection**: Behavioral anomalies like unauthorized packet crafting from non-admin processes.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scapy]] (for general packet crafting)
- [[tools/thm-ipv6-toolkit]] (IPv6-specific attack suite)

## References

- Official GitHub Repository: https://github.com/vitlabuda/randicmp6
- IPv6 Security Considerations: RFC 7113
- Related Research: Black Hat talks on IPv6 attacks
