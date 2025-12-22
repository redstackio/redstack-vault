---
id: 29ba94e7-6450-42e8-822b-2a91b540ae0e
type: tool
verified: true
created_at: '2019-08-28T21:17:20.935195+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - reconnaissance
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=airserv-ng'
validated: true
---

# airserv-ng

**Status**: Unverified

## Overview

airserv-ng is a wireless card server from the Aircrack-ng suite that enables multiple wireless applications to share a single wireless interface over a TCP network connection. It abstracts OS and driver-specific details into the server, allowing remote clients to perform wireless operations without local hardware access. Commonly used in penetration testing for distributed wireless attacks or virtualized environments.

## Description

airserv-ng operates as a TCP server, binding to a specified port on the host machine. Clients (like airodump-ng or aireplay-ng) connect via TCP to issue wireless commands as if directly accessing the card. This is useful for scenarios where the wireless hardware is on a separate machine, such as headless servers or when running tools in containers/VMs without direct USB passthrough. It supports monitor mode and injection, making it essential for wireless reconnaissance and attacks.

## Features

- Feature 1: TCP-based remote access to wireless interfaces, eliminating driver compatibility issues for clients.
- Feature 2: Supports multiple simultaneous client connections for parallel wireless operations.
- Feature 3: Channel locking and interface management, compatible with most Linux wireless drivers (e.g., ath9k, rtl8187).
- Feature 4: Integration with Aircrack-ng tools for seamless remote packet capture and injection.

## Installation

### Requirements

- Linux kernel with wireless extensions support.
- Compatible wireless adapter (e.g., Alfa AWUS036N).
- Aircrack-ng suite (airserv-ng is included).

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# From source (optional)
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make
sudo make install
```

## Basic Usage

```bash
airserv-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --dev <ifname> | Specify the wireless interface |
| -p, --port <port> | TCP port to bind (default 1080) |
| -C, --ch <channel> | Lock to specific channel |
| -h, --help | Show help |

## Examples

### Example 1: Basic Usage

Start server on wlan0, default port:

```bash
airserv-ng -d wlan0
```

Connect from client: `airodump-ng tcp://192.168.1.100:1080`

### Example 2: Advanced Usage

Start with channel lock:

```bash
airserv-ng -d wlan0 -p 7000 -C 11
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless network discovery)
- [[File and Directory Discovery]] File and Directory Discovery (extended to wireless interfaces)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for airserv-ng processes via `ps aux | grep airserv` or unusual TCP listeners on ports like 1080/7000.
- Detection method 2: Network traffic analysis showing TCP connections to wireless server ports from pentest tools.
- Detection method 3: Wireless interface in monitor mode (`iwconfig` shows mode).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]]
- [[tools/airodump-ng]]
- [[tools/aireplay-ng]]

## References

- Official documentation: https://www.aircrack-ng.org/doku.php?id=airserv-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
