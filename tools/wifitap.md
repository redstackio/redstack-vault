---
id: f84354b6-4f67-4572-bfa8-4ae624aec68a
type: tool
verified: true
created_at: '2019-08-28T21:17:27.736562+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - wifi
  - injection
  - kernel-module
  - network-evasion
  - traffic-capture
url: 'https://github.com/Segfault-Inc/wifitap'
validated: true
---

# wifitap

**Status**: Unverified

## Overview

Wifitap is a proof-of-concept Linux kernel module for establishing IP communication over WiFi networks using 802.11 traffic capture and injection. It creates a virtual TAP interface (default: wj0) that allows applications to send and receive IP packets without relying on standard WiFi associations, enabling bypass of access point restrictions like client isolation.

Common use cases in security testing include injecting arbitrary packets into WiFi frames, evading inter-client communication blocks (e.g., Cisco PSPF), and accessing hidden or multiple SSIDs on the same AP.

## Description

Wifitap operates by linking a monitor-mode WiFi interface to a virtual TAP device. Once loaded, it captures 802.11 frames on the monitor interface and injects them back, tunneling IP traffic through the WiFi medium. This approach requires no special userland libraries for injection and works with compatible WiFi chipsets supporting monitor mode (e.g., Atheros ath9k_htc). It is particularly useful for layer 2 attacks or C2 channels in environments with restricted wired/wireless access.

## Features

- Virtual TAP interface for IP over 802.11 tunneling
- Bypasses AP-level restrictions like client isolation (PSPF) and SSID segmentation
- Supports arbitrary packet injection without proprietary libraries
- Configurable monitor and TAP interfaces
- Debug mode for troubleshooting injection/capture issues

## Installation

### Requirements

- Linux kernel with mac80211 and cfg80211 modules
- WiFi adapter supporting monitor mode and packet injection (e.g., Alfa AWUS036N with ath9k)
- Development tools: gcc, make, kernel headers (`sudo apt install linux-headers-$(uname -r)` on Ubuntu)
- Root privileges for module loading and interface configuration

### Install Commands

```bash
# Clone the repository
[[commands/git-clone-wifitap-repo]]

# Compile the module
cd wifitap
[[commands/compile-wifitap-module]]

# Load the module (adjust interfaces)
sudo insmod wifitap.ko mon_if=mon0 tap_if=wj0

# Setup the TAP interface
[[commands/setup-wj0-interface]]
```

## Basic Usage

```bash
# Create monitor interface first (using iw)
sudo iw phy phy0 interface add mon0 type monitor
sudo ifconfig mon0 up

# Load module (as above)

# Test connectivity (e.g., ping via wj0)
sudo ip route add default via 192.168.1.1 dev wj0
ping 192.168.1.1
```

### Common Options

| Option | Description |
|--------|-------------|
| mon_if | Monitor interface name (default: mon0) |
| tap_if | TAP interface name (default: wj0) |
| debug | Enable debug output (1=on) |

## Examples

### Example 1: Basic Setup and Test

1. Clone and compile as above.
2. Load: `sudo insmod wifitap.ko mon_if=mon0 tap_if=wj0`
3. Setup: `sudo ip link set wj0 up && sudo ip addr add 192.168.1.100/24 dev wj0`
4. Route traffic: `sudo ip route add 192.168.1.0/24 dev wj0`
5. Test: Run `tcpdump -i wj0` to monitor injected traffic.

### Example 2: Advanced Usage with Injection

Use the wj0 interface to route application traffic (e.g., nc listener) through WiFi injection to bypass AP isolation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Non-Application Layer Protocol]] Non-Application Layer Protocol (for C2 over WiFi injection)
- [[Archive via Utility]] Archive Collected Data: Traffic Tunneling (for data exfiltration via custom channels)

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Kernel module loaded: `lsmod | grep wifitap`
- Unusual TAP interface: `ip link show | grep wj0`
- Monitor mode on WiFi: `iw dev | grep monitor`
- Injection traffic: High volume of 802.11 management frames or anomalous packet rates on AP logs
- Kernel taint from out-of-tree module

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]] (for WiFi monitoring and injection)
- [[scapy]] (for packet crafting and injection)

## References

- Official GitHub: https://github.com/Segfault-Inc/wifitap
- Kernel module documentation in repo README
