---
id: 67c33acf-1018-4d21-acfb-daef74e76dba
type: tool
verified: true
created_at: '2019-08-28T21:17:25.645298+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - mitm
  - update-compromise
  - adversary-in-the-middle
url: 'https://github.com/thisisevil/evilgrade'
commands:
  - '[[commands/evilgrade-launch]]'
  - '[[commands/evilgrade-daemon-mode]]'
validated: true
---

# Evilgrade

**Status**: Unverified

## Overview

Evilgrade is a modular framework that exploits vulnerabilities in software update mechanisms by performing man-in-the-middle attacks to inject and serve fake updates, enabling the delivery of malicious payloads to target systems.

## Description

Evilgrade allows attackers to intercept update requests and respond with tampered updates, tricking applications into installing malware instead of legitimate patches. It supports various modules for popular software like Adobe products, Java, and iTunes, making it suitable for network-based attacks where update traffic can be spoofed. The tool integrates ARP poisoning for positioning and provides an interactive interface for configuration.

## Features

- Modular plugins for targeting specific software update protocols
- ARP spoofing capabilities for MITM positioning
- Customizable fake update payloads and responses
- Real-time monitoring of intercepted traffic and attack progress
- Support for HTTP/HTTPS downgrade attacks on updates

## Installation

### Requirements

- Python 2.7 (note: legacy tool, may require compatibility fixes on modern systems)
- Scapy library for packet crafting
- Root/admin privileges for network interface manipulation
- Compatible with Kali Linux or Debian-based distributions

### Install Commands

```bash
# On Kali Linux (available in repositories)
sudo apt update && sudo apt install evilgrade

# Manual installation from source
sudo apt install git python2 scapy
cd /opt
git clone https://github.com/thisisevil/evilgrade.git
git checkout python2  # For Python 2 compatibility
cd evilgrade
sudo python2 setup.py install
```

## Basic Usage

```bash
evilgrade --help
```

Launches the help menu showing available options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help information and exit |
| -d, --daemon | Run Evilgrade in daemon (background) mode |
| -i, --interface | Specify the network interface to use (e.g., eth0) |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

```bash
sudo evilgrade-launch
```

This starts the interactive menu where you can select modules, configure targets, and initiate attacks.

### Example 2: Advanced Usage

```bash
sudo evilgrade-daemon-mode -i eth0
```

Runs Evilgrade in the background on a specific interface for persistent monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Compromise Software Supply Chain]] Compromise Software Supply Chain

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous ARP traffic indicating poisoning (e.g., gratuitous ARP replies)
- Suspicious HTTP requests to legitimate update servers redirected to attacker-controlled IPs
- Unexpected software installations or update failures on endpoints
- Process monitoring for 'evilgrade' or Python 2 scripts with Scapy imports
- Network logs showing spoofed update responses

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ettercap]] (for ARP spoofing and MITM)
- [[tools/bettercap]] (modern MITM framework alternative)
- [[tools/Responder]] (for LLMNR/NBT-NS poisoning)

## References

- Official GitHub Repository: https://github.com/thisisevil/evilgrade
- Original Project Site: http://www.evilgrade.net/
- Kali Linux Documentation: https://tools.kali.org/information-gathering/evilgrade
