---
id: 50efc607-3ff7-49d1-a670-4a216e69d777
type: tool
verified: true
created_at: '2020-02-19T23:14:12.987926+00:00'
updated_at: '2023-05-30T01:09:50.013875+00:00'
commands:
  - '[[commands/ssh-lan-turtle-initial-setup]]'
tags:
  - Hardware
  - Social Engineering
platforms:
  - Hardware
url: 'https://shop.hak5.org/products/lan-turtle'
description: >-
  A compact hardware implant that provides stealthy remote access, network
  reconnaissance, and man-in-the-middle capabilities when plugged into a target
  network.
validated: true
---

# Lan-Turtle

**Status**: ✓ Verified

## Overview

The Lan Turtle is a USB Ethernet adapter-sized hardware device from Hak5 designed for penetration testing and red team operations. It emulates a keyboard and network interface, allowing attackers to deploy it physically on a target network for covert remote access, traffic interception, and intelligence gathering. Common use cases include physical drop deployments in social engineering scenarios to establish persistent backdoors or monitor network activity without detection.

## Description

Once plugged into a network port or device via RJ-45, the Lan Turtle appears as a legitimate network device while providing a backdoor SSH interface over USB to the attacker's machine. It supports modules for advanced functionality like SSH tunneling (AutoSSH), packet capture, and ARP spoofing for MITM attacks. The device runs a lightweight Linux-based OS with a simple shell and configuration menu, making it accessible for field deployments. It is particularly useful in environments where remote access is restricted, enabling attackers to bypass firewalls and gain internal network visibility.

## Features

- **Stealth Remote Access**: USB HID emulation for initial setup and persistent SSH over USB.
- **Network Intelligence**: Built-in modules for traffic sniffing, credential capture, and service enumeration.
- **Man-in-the-Middle**: Supports ARP poisoning and SSL stripping for intercepting communications.
- **Modular Design**: Extensible with payloads and scripts for custom behaviors like keylogging or beaconing.
- **Portable and Discreet**: Compact form factor (fits in a pocket) with low power consumption for long-term deployments.

## Installation

### Requirements

- RJ-45 Ethernet cable for network connection.
- Attacker-controlled computer with USB port and SSH client (e.g., Kali Linux).
- Network access in the 172.16.84.0/24 range for initial USB connection (DHCP supported).
- Internet access on the attacker machine for firmware updates.

### Setup Steps

1. **Hardware Connection**: Connect one end of the RJ-45 cable to your router or target network port, and plug the USB end into your attacker computer. The device will request an IP in the 172.16.84.0/24 subnet via USB networking.

2. **Initial SSH Access**: Use the default credentials to connect via SSH. Execute [[commands/ssh-lan-turtle-initial-setup]] to log in with username `root` and password `sh3llz`. Once connected, immediately change the password:

   ```bash
   passwd
   ```

   Enter a strong new password when prompted.

3. **Configure WAN Interface**: In the Lan Turtle shell, access the configuration menu by typing `config`. Navigate to "Change WAN IP Settings" and select DHCP to enable internet access through the network port.

4. **Update Firmware**: Still in the config menu, select "Check for Updates" to download and apply the latest software releases. This ensures access to new modules and security patches.

5. **Verification**: Confirm internet connectivity by pinging an external host (e.g., `ping 8.8.8.8`). The device is now ready for module installation and payload deployment.

Note: Full documentation and module downloads are available via the Hak5 website after setup.

## Basic Usage

After initial setup, the Lan Turtle provides a root shell for running modules. Common starting point:

```bash
config
```

This launches the graphical configuration shell for managing network settings, modules, and payloads.

### Common Options

| Option | Description |
|--------|-------------|
| `config` | Launch the configuration menu for IP, updates, and modules. |
| `modules` | List and install available payloads (requires internet). |
| `autossh` | Enable persistent SSH tunneling for remote access. |
| `help` | Show available commands and usage. |

## Examples

### Example 1: Basic Connection and Config

1. Connect hardware as described.
2. Run [[commands/ssh-lan-turtle-initial-setup]].
3. In shell: `config` to open menu and set WAN to DHCP.

### Example 2: Deploy a Module

After updates:

```bash
modules install surveillance
```

Activates network monitoring payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Replication Through Removable Media]] Replication Through Removable Media (for physical deployment).
- [[Encrypted Channel]] Encrypted Channel (via SSH tunneling).
- [[SSH]] Remote Services::SSH (for backdoor access).

### Tactics

- [[Persistence]] Persistence (hardware implant for ongoing access).
- [[Command and Control]] Command and Control (stealthy C2 over USB/network).

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB Ethernet devices in network logs or endpoint detection.
- Traffic from 172.16.84.0/24 subnet over USB interfaces.
- SSH connections from unknown hardware MAC addresses.
- Anomalous ARP activity or MITM signatures in packet captures.
- Physical security logs showing unauthorized device insertions.

## Related Procedures

No direct procedures linked yet; refer to Hak5 documentation for payload-specific guides.

## Related Tools

- [[USB-Rubber-Ducky]] (Companion Hak5 device for keystroke injection).
- [[Bash-Bunny]] (Advanced multi-tool USB implant).

## References

- Official Hak5 Documentation: https://docs.hak5.org/lan-turtle/
- Firmware Downloads: https://shop.hak5.org/pages/lan-turtle
- Community Payloads: Hak5 Forums and GitHub repositories.
