---
type: tool
verified: true
description: >-
  BetterCAP is a powerful, modular network attack and monitoring framework for
  performing man-in-the-middle attacks, traffic sniffing, and network
  reconnaissance.
url: 'https://www.bettercap.org/'
platforms:
  - Linux
  - macOS
tags:
  - mitm
  - spoofing
  - reconnaissance
  - network-attack
commands:
  - '[[commands/bettercap-launch-basic]]'
  - '[[commands/bettercap-launch-with-interface]]'
  - '[[commands/bettercap-launch-mitm-target]]'
  - '[[commands/bettercap-run-caplet]]'
validated: true
---

# bettercap

**Status**: Unverified

## Overview

BetterCAP is a next-generation, modular, and dynamic network probing and attack framework written in Go. It is designed as a Swiss Army knife for network security testing, supporting a wide range of attacks including ARP/NDP spoofing, DNS manipulation, traffic sniffing, and man-in-the-middle (MITM) operations. Commonly used in red team engagements for network reconnaissance and interception.

## Description

BetterCAP succeeds tools like Ettercap and provides an interactive console for enabling modules dynamically. It supports Ethernet, WiFi, Bluetooth Low Energy (BLE), and more, making it versatile for wired and wireless environments. Key capabilities include passive and active network discovery, session hijacking, credential harvesting via proxies, and injection attacks. It is portable across platforms but excels on Linux-based systems like Kali.

## Features

- **Spoofing Modules**: ARP, NDP, and HSRP spoofing for traffic redirection.
- **Proxy Support**: HTTP/HTTPS proxies for intercepting and modifying web traffic.
- **Sniffing and Analysis**: Packet capture with protocol dissection (e.g., pcap output).
- **Reconnaissance**: Host discovery, service enumeration, and OS fingerprinting.
- **Automation via Caplets**: Scriptable configurations for common scenarios like full MITM setups.
- **Extensibility**: Modular design allows custom modules and integrations.

## Installation

### Requirements

- Go 1.16+ (for building from source)
- Root/admin privileges for network operations
- Compatible network drivers (e.g., for WiFi monitor mode)

### Install Commands

```bash
# Kali Linux (pre-installed in recent versions)
sudo apt update && sudo apt install bettercap

# Ubuntu/Debian
sudo apt install golang-go
go install github.com/bettercap/bettercap@latest
sudo cp ~/go/bin/bettercap /usr/local/bin/

# From source (all platforms)
git clone https://github.com/bettercap/bettercap.git
cd bettercap
make build
sudo make install

# macOS with Homebrew
go install github.com/bettercap/bettercap@latest
```

## Basic Usage

```bash
bettercap -h
```

This displays help and available options.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-iface INTERFACE` | Select network interface |
| `-T TARGET` | Set targets (IP or CIDR) |
| `-caplet FILE` | Load a caplet file for automation |
| `-eval "COMMAND"` | Execute command on startup |
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage

Launch interactive console:

```bash
bettercap
```

See [[commands/bettercap-launch-basic]] for details.

### Example 2: Advanced Usage

Targeted MITM on a network:

```bash
bettercap -T 192.168.1.0/24 -iface eth0 -eval "arp.spoof on; net.sniff on"
```

See [[commands/bettercap-launch-mitm-target]] for launch and related modules.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Network Sniffing]] Network Sniffing
- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Web Protocols]] Application Layer Protocol: Web Protocols

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ARP traffic or duplicate IP responses (spoofing detection via ARPwatch).
- Unexpected proxy connections or SSL stripping (HSTS enforcement, certificate pinning).
- High network interface usage or pcap file creation in /tmp.
- Process monitoring for 'bettercap' binary with elevated privileges.
- Anomaly in DNS queries or HTTP redirects.

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
- [[tools/Wireshark]]
- [[tools/tcpdump]]

## References

- Official documentation: https://www.bettercap.org/
- GitHub repository: https://github.com/bettercap/bettercap
- MITM scenarios: BetterCAP caplets in /usr/share/bettercap/caplets/
