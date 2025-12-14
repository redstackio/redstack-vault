---
id: tool-responder
url: 'https://github.com/lgandx/Responder'
tags:
  - ntlm-capture
  - poisoning
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.361Z'
validated: true
submitted: true
---
# Responder

**Status**: Unverified

## Overview

Responder is a LLMNR, NBT-NS, and MDNS poisoner tool for capturing NetNTLM hashes from network authentication attempts in Windows environments.

## Description

Used in offensive security to exploit misconfigurations in name resolution, Responder listens for broadcasts and responds with fake servers to relay or capture creds. In this attack, it captures hashes triggered by file:// SMB in Burp's HTML injection.

## Features

- Feature 1: Poisons LLMNR/NBT-NS/MDNS queries
- Feature 2: Captures NTLMv1/v2 hashes and relays
- Feature 3: Supports HTTP/SMB/FTP poisoning

## Installation

### Requirements

- Python 2.7+ or 3.x
- Scapy library

### Install Commands

```bash
# Clone repo
git clone https://github.com/lgandx/Responder.git
cd Responder
pip install -r requirements.txt
```

## Basic Usage

```bash
python Responder.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -I | Interface to listen on |
| -w | Enable WPAD poisoning |
| -r | Enable NBT-NS relay |

## Examples

### Example 1: Basic Usage

```bash
python Responder.py -I eth0
```

### Example 2: Advanced Usage

```bash
python Responder.py -I eth0 -w -r -d
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and Relay

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious UDP traffic on 5355 (LLMNR)
- Fake server responses in Wireshark
- Hash capture logs on attacker host

## Related Procedures


## Related Tools

- [[tools/ntlmrelayx]]
- [[tools/Inveigh]]

## References

- Official documentation: https://github.com/lgandx/Responder
- Related resources: Impacket integration
