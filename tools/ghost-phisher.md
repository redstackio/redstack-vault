---
id: 7f858e95-2b97-4fe6-b0ae-31376de387ca
name: Ghost-Phisher
type: tool
verified: true
created_at: '2019-08-28T21:17:37.948288+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - phishing
  - auditing
  - mitm
  - ap-emulation
url: 'https://github.com/Kenjith/ghost-phisher'
validated: true
---

# Ghost-Phisher

**Status**: Unverified

## Overview

Ghost Phisher is a Python-based GUI tool for wireless and Ethernet security auditing, designed to emulate access points (APs), host phishing pages, and perform man-in-the-middle (MITM) attacks. It is commonly used in penetration testing for assessing Wi-Fi security, credential harvesting, and network interception in controlled environments.

## Description

Built using Python and the Qt GUI library, Ghost Phisher enables auditors to create rogue access points, deploy credential-logging webpages, and integrate with tools like Metasploit for deeper exploitation. Key capabilities include emulating Wi-Fi APs to lure clients, running integrated HTTP/DNS/DHCP servers for seamless network integration, and supporting passive/active session hijacking and ARP poisoning. Credentials are automatically logged to an SQLite database. Note: This tool is older and may require updates for modern hardware/drivers; use ethically in authorized testing only.

## Features

- **HTTP Server**: Hosts custom webpages for phishing attacks, capturing form submissions.
- **RFC 1035 DNS Server**: Resolves domains to attacker-controlled IPs for redirection.
- **RFC 2131 DHCP Server**: Assigns IP addresses to connected clients, enabling network control.
- **Webpage Hosting and Credential Logger**: Deploys phishing sites with SQLite-backed logging.
- **WiFi Access Point Emulator**: Creates fake APs using hostapd integration.
- **Session Hijacking**: Supports passive (Ethernet) and active modes for intercepting traffic.
- **ARP Cache Poisoning**: Performs MITM and DoS via ARP spoofing.
- **Metasploit Bindings**: Integrates with Metasploit for payload delivery post-capture.
- **Automatic Credential Logging**: Stores captured data in SQLite for easy export.
- **Update Support**: Built-in updater for maintaining the tool.

## Installation

### Requirements

- Python 3.x with PyQt5
- Wireless network adapter supporting AP mode (e.g., monitor/injection capable)
- hostapd and dnsmasq for AP/DHCP functionality
- Metasploit Framework (optional for advanced features)
- Root/admin privileges for network interface manipulation

### Install Commands

On Kali Linux (pre-installed in older versions; may need manual setup):

```bash
# Update system
apt update

# Install dependencies
apt install python3-pyqt5 hostapd dnsmasq metasploit-framework

# Clone from GitHub if not present
git clone https://github.com/Kenjith/ghost-phisher.git
cd ghost-phisher

# Run setup (if available)
python3 setup.py install
```

For Ubuntu/Debian:

```bash
apt install python3-pyqt5 hostapd dnsmasq
# Then clone and install as above
```

Manual setup may be required for compatibility with modern kernels; check compatibility with airmon-ng for wireless interfaces.

## Basic Usage

```bash
tool-name --help
```

Ghost Phisher is primarily GUI-driven; launch via command line to open the interface.

### Common Options

| Option | Description |
|--------|-------------|
| No CLI flags | GUI launch only; configurations done via tabs in interface |
| Run as root | Required: `sudo python3 ghost.py` for network access |

## Examples

### Example 1: Basic Usage

Launch the GUI:

```bash
sudo python3 /usr/share/ghost-phisher/ghost.py
```

In the GUI, select 'Integrated Access Point' tab, configure SSID/interface, and start the AP.

### Example 2: Advanced Usage

For phishing setup:

1. Launch GUI as above.
2. Go to 'HTTP Server' tab, load a phishing template (e.g., router login page).
3. Enable DNS/DHCP servers.
4. Start AP and monitor connections in the interface.

Use [[commands/ghost-phisher-launch-gui]] for scripted launch.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control (for privilege escalation in AP setup)
- [[T1566.001]] Phishing: Spearphishing Attachment (via hosted webpages)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Tactics

- [[Initial Access]] Initial Access (via phishing)
- [[Discovery]] Discovery (network enumeration)
- [[Command and Control]] Command and Control (AP emulation)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual wireless SSIDs or rogue APs (monitor with tools like airodump-ng).
- Suspicious DHCP/DNS traffic from non-standard servers.
- Python/Qt processes with network binding (e.g., `ps aux | grep ghost`).
- SQLite databases with credential logs in temp directories.
- ARP table anomalies indicating poisoning.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Airgeddon]] (alternative AP toolkit)
- [[tools/Metasploit]] (for payload integration)
- [[tools/Hostapd]] (underlying AP emulator)

## References

- Official GitHub: https://github.com/Kenjith/ghost-phisher
- PyQt Documentation: https://www.riverbankcomputing.com/software/pyqt/intro
- Ethical usage guidelines: Always obtain permission before testing.
