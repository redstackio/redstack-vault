---
id: da51acdd-f2ea-4244-b5bd-a191efacb28e
type: tool
verified: true
created_at: '2019-08-28T21:17:19.156815+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - wireless
  - packet-forging
  - injection
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=packetforge-ng'
commands:
  - '[[commands/packetforge-ng-forge-arp-request]]'
  - '[[commands/packetforge-ng-forge-udp-packet]]'
validated: true
---

# packetforge-ng

**Status**: Unverified

## Overview

packetforge-ng is a command-line utility from the Aircrack-ng suite designed to generate forged and encrypted packets for injection into wireless networks. It is primarily used in wireless penetration testing to create packets like ARP requests, UDP, ICMP, or custom types that can be injected to facilitate attacks such as deauthentication, replay, or session hijacking. Common use cases include forging ARP packets for ARP poisoning in WEP cracking or UDP packets for testing network responses in monitored Wi-Fi environments.

## Description

packetforge-ng allows users to construct packets that mimic legitimate traffic but are encrypted using keys captured from the target network (e.g., via airodump-ng). This makes the forged packets indistinguishable from real ones during injection with tools like aireplay-ng. It supports various packet types through numeric flags (-0 for ARP requests, -1 for UDP, etc.) and requires input like MAC addresses, ESSID, and packet length. The tool is essential for advanced wireless attacks where direct packet crafting is needed, but it requires a compatible wireless interface in monitor mode.

## Features

- Forge multiple packet types: ARP requests/replies, UDP, ICMP echo requests, and custom packets.
- Encrypt packets using WEP or WPA keys captured from the network.
- Specify transmission details like rate, length, and interface index.
- Output forged packets in pcap format for direct injection or analysis.
- Support for source/destination MAC, IP, and port customization in advanced packet types.

## Installation

### Requirements

- Linux kernel with wireless extensions support.
- Compatible wireless adapter (e.g., Atheros AR9271) that supports monitor mode and packet injection.
- Aircrack-ng suite dependencies (libpcap, libssl).

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update

# On Ubuntu/Debian
sudo apt update && sudo apt install aircrack-ng

# From source (if needed)
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make && sudo make install
```

## Basic Usage

```bash
packetforge-ng --help
```

This displays all available options, packet types, and syntax examples.

### Common Options

| Option | Description |
|--------|-------------|
| `-0` | Forge ARP request packet |
| `-1` | Forge UDP packet |
| `-a <mac>` | Access Point MAC address |
| `-h <mac>` | Source/client MAC address |
| `-d <mac>` | Destination MAC address (for UDP/ICMP) |
| `-l <len>` | Packet length in bytes |
| `-y <essid>` | Network ESSID |
| `-x <rate>` | Transmission rate (e.g., 1 for 1Mbps) |
| `-i <index>` | Interface index (0 for first) |
| `-o <file>` | Output pcap file |
| `-k <key>` | WEP key for encryption (hex format) |
| `-b <bssid>` | BSSID for the packet |
| `-e <essid>` | ESSID in plaintext |
| `-p <file>` | Input pcap for key derivation |
| `-u` | Use unencrypted mode |
| `-9` | Custom packet from hex input |

## Examples

### Example 1: Basic Usage

Forge a simple ARP request packet using a captured key file.

```bash
packetforge-ng -0 -a 00:11:22:33:44:55 -h AA:BB:CC:DD:EE:FF -l 64 -y "MyNetwork" -x 1 -i 0 -o arp-request.cap -p capture.cap
```

### Example 2: Advanced Usage

Forge a UDP packet with specific IP/port details for testing.

```bash
packetforge-ng -1 -a 00:11:22:33:44:55 -h AA:BB:CC:DD:EE:FF -d 11:22:33:44:55:66 -l 100 -y "MyNetwork" -x 2 -S 12345 -D 80 -f 192.168.1.100 -t 192.168.1.1 -P "test payload" -i 0 -o udp-packet.cap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Direct Network Flood]] Direct Network Flood (for deauthentication via injected packets)
- [[Credentials in Files]] Password Policy Discovery (in context of wireless credential cracking)
- [[Disable or Modify Tools]] Disable or Modify Tools (impairing wireless security through injection)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Impact]] Impact

## Detection

- Monitor wireless traffic for anomalous packet rates or forged MAC/IP combinations using tools like Wireshark or Kismet.
- Enable wireless intrusion detection systems (WIDS) to alert on injection attempts or unusual ARP/UDP floods.
- Log interface monitor mode activations and correlate with packetforge-ng processes (e.g., via procmon).
- Network logs showing sudden deauth frames or replayed packets from unknown sources.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aireplay-ng]] (for injecting the forged packets)
- [[tools/airodump-ng]] (for capturing keys and ESSIDs)
- [[tools/aircrack-ng]] (for cracking and analysis)

## References

- Official Documentation: https://www.aircrack-ng.org/doku.php?id=packetforge-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
- Wireless Penetration Testing Guide: https://www.aircrack-ng.org/
