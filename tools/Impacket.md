---
url: 'https://github.com/SecureAuthCorp/impacket'
tags:
  - smb
  - ntlm
  - protocol
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-04'
updated_at: '2025-12-14T03:53:38.750Z'
id: 29d9c48c-95d1-45b7-ad34-f2f230bc01a7
validated: true
submitted: true
---
# Impacket

**Status**: Unverified

## Overview

Impacket is a collection of Python classes for working with network protocols, primarily used in offensive security for SMB, NTLM, and Kerberos operations, including server emulation for capturing credentials in SSRF scenarios.

## Description

Impacket provides tools like smbserver.py to simulate SMB shares, forcing authentication and logging NTLM hashes. It's essential for exploiting protocol weaknesses, relaying creds, and testing auth in environments like Windows networks. Commonly used in red teaming for pass-the-hash and relay attacks.

## Features

- Feature 1: SMB client/server emulation with NTLM support
- Feature 2: Kerberos ticket manipulation and golden/silver tickets
- Feature 3: Protocol dissection for Wireshark integration

## Installation

### Requirements

- Python 3.6+
- pip

### Install Commands

```bash
pip install impacket
# Or from source
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip install .
```

## Basic Usage

```bash
python3 -m impacket.smbserver --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-debug` | Verbose logging |
| `-smb2support` | Enable SMB2 protocol |

## Examples

### Example 1: Basic Usage

```bash
python3 smbserver.py SHARE /tmp/share
```

### Example 2: Advanced Usage

```bash
python3 smbserver.py SHARE /tmp/share -debug -username attacker -password pass
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Adversary-in-the-Middle]]

### Tactics

- [[Initial Access]]
- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes with impacket modules
- Unusual SMB server instances on non-DC systems
- Network logs showing SMBv1/v2 auth from unexpected sources

## Related Procedures

- [[procedures/Setup-Impacket-SMB-Server-for-NTLM-Capture]]

## Related Tools

- [[Responder]]
- [[CrackMapExec]]

## References

- Official GitHub: https://github.com/SecureAuthCorp/impacket
- Impacket documentation
