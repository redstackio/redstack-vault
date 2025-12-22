---
type: tool
description: >-
  A Python-based tool for spoofing SSDP responses to perform network phishing
  attacks and capture NTLM hashes from Windows clients.
url: 'https://github.com/mgeeky/Evil-SSDP'
verified: true
platforms:
  - Linux
  - Windows
tags:
  - phishing
  - ssdp
  - upnp
  - ntlm
  - credential-access
commands:
  - '[[commands/evil-ssdp-start-basic-server]]'
  - '[[commands/evil-ssdp-with-custom-template]]'
validated: true
---

# evil-ssdp

**Status**: Unverified

## Overview

evil-ssdp is a security testing tool designed to spoof Simple Service Discovery Protocol (SSDP) responses on a local network. It creates a fake Universal Plug and Play (UPnP) device advertisement, tricking Windows clients into connecting to a controlled phishing server that captures NTLM authentication hashes. This is useful for red team simulations of network-based credential phishing.

## Description

The tool listens for SSDP multicast discovery packets (M-SEARCH) sent by clients searching for UPnP devices. It responds with forged NOTIFY and reply packets pointing to a locally hosted phishing page mimicking a legitimate device authentication prompt. When victims attempt to authenticate, their NTLM hashes are captured for offline cracking or relay attacks. It leverages Scapy for packet crafting and Flask for the web server, making it effective in Windows-heavy environments where SSDP/UPnP is commonly enabled.

## Features

- Automatic spoofing of SSDP M-SEARCH responses with fake UPnP device details
- Built-in phishing web server for NTLM hash extraction
- Support for custom phishing templates and icons to increase believability
- Multi-interface listening for complex network setups
- Logging of captured credentials and victim interactions
- Integration with hash cracking tools via output formats

## Installation

### Requirements

- Python 3.6+
- Scapy library for packet manipulation
- Flask for the web server
- Root/admin privileges for raw socket access

### Install Commands

```bash
# Clone the repository
git clone https://github.com/mgeeky/Evil-SSDP.git
cd Evil-SSDP

# Install Python dependencies
pip3 install -r requirements.txt
```

On Kali Linux, most dependencies are pre-installed or available via apt.

## Basic Usage

```bash
python3 evil_ssdp.py --help
```

This displays available options, including interface selection and server configuration.

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the network interface (e.g., eth0) |
| --lhost | Local host IP for the phishing server (default: 0.0.0.0) |
| --lport | Local port for the phishing server (default: 80) |
| --template-dir | Directory with custom phishing templates |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Start the server on the default interface:

```bash
python3 evil_ssdp.py -i eth0
```

### Example 2: Advanced Usage

Run with custom templates and specific binding:

```bash
python3 evil_ssdp.py -i wlan0 --lhost 192.168.1.100 --lport 8080 --template-dir ./phish_templates/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.002]] Spearphishing Link
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SSDP multicast traffic (239.255.255.250:1900) from non-standard sources
- Inbound HTTP connections to local ports (e.g., 80, 8080) with NTLM authentication attempts
- Anomalous UPnP device advertisements on the network
- Log analysis for Flask/Scapy processes or Python scripts sending forged packets
- Network monitoring for redirects to local phishing domains/IPs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Responder]] (for LLMNR/NBT-NS poisoning)
- [[tools/Inveigh]] (Windows-based NTLM relay)

## References

- Official GitHub: https://github.com/mgeeky/Evil-SSDP
- Blog Post: https://posts.specterops.io/evil-ssdp-redirecting-users-to-phishing-sites-via-rogue-upnp-8c0ce7d4b1a5
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1566/002/
