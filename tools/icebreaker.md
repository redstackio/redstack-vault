---
id: e9be40ad-d9dd-46c4-9036-f5012b71f0b6
name: icebreaker
type: tool
verified: true
created_at: '2019-08-28T21:17:42.239085+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - credential-access
  - ntlm
  - llmnr
  - nbt-ns
  - ad
url: 'https://github.com/Maz-Maz/icebreaker'
validated: true
---

# icebreaker

**Status**: Unverified

## Overview

Icebreaker is a Python-based tool designed to capture plaintext Active Directory credentials or NTLM hashes by spoofing LLMNR (Link-Local Multicast Name Resolution) and NBT-NS (NetBIOS Name Service) responses on internal networks. It is particularly useful for red team engagements where the attacker has network access but lacks domain credentials, allowing opportunistic capture of authentication attempts from Windows clients.

## Description

Icebreaker operates as an adversary-in-the-middle tool that monitors multicast traffic for name resolution queries from Windows machines. When a query is detected (e.g., for a non-existent hostname), it responds with a spoofed IP pointing back to itself, prompting the victim machine to authenticate via NTLM. This can yield usernames, domains, NTLM hashes, or even plaintext passwords if the target is misconfigured. It is effective in environments where LLMNR and NBT-NS are enabled (default on Windows) and is commonly used in lateral movement or initial access scenarios within AD networks.

## Features

- Feature 1: LLMNR and NBT-NS query interception and spoofing
- Feature 2: Real-time capture of NTLMv1/v2 hashes and potential plaintext credentials
- Feature 3: Support for WPAD (Web Proxy Auto-Discovery) poisoning to capture additional auth attempts
- Feature 4: Verbose logging and hash export for offline cracking

## Installation

### Requirements

- Python 3.6+
- Scapy library for packet manipulation
- Root/admin privileges for raw socket access

### Install Commands

```bash
# Clone the repository
git clone https://github.com/Maz-Maz/icebreaker.git
cd icebreaker

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (pre-requisites often satisfied)
apt update && apt install python3-scapy
```

On Windows, use a compatible Python environment like via WSL or Cygwin, ensuring Npcap is installed for packet capture.

## Basic Usage

```bash
python3 icebreaker.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the network interface to listen on |
| -v, --verbose | Enable verbose output for debugging |
| --wpad | Enable WPAD poisoning for proxy auth capture |
| -o, --output | Save captured hashes to a file |

## Examples

### Example 1: Basic Usage

```bash
python3 icebreaker.py -i eth0
```

Listens on eth0 for queries and captures any NTLM auth attempts.

### Example 2: Advanced Usage

```bash
python3 icebreaker.py -i eth0 -v --wpad -o captured_hashes.txt
```

Captures hashes with WPAD support, verbose logging, and outputs to file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and Relay
- [[Password Filter DLL]] Modify Authentication Process: Network Device Authentication
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Credential Access]] Credential Access
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual multicast traffic spikes on LLMNR (UDP 5355) or NBT-NS (UDP 137) ports
- Detection method 2: Monitoring for spoofed IP responses in name resolution logs (e.g., via Wireshark or endpoint EDR)
- Detection method 3: NTLM authentication failures or unexpected hash captures in security event logs (Event ID 4625)
- Detection method 4: Disable LLMNR via Group Policy (Computer Configuration > Administrative Templates > Network > DNS Client > Turn off multicast name resolution)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Responder]]
- [[tools/Inveigh]]

## References

- Official GitHub: https://github.com/Maz-Maz/icebreaker
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1557/001/
- Blog Post: Original tool description and usage guide
