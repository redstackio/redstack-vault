---
id: tool-samba
url: 'https://www.samba.org/'
tags:
  - file-sharing
  - smb
  - hosting
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.530Z'
validated: true
submitted: true
---
# Samba

**Status**: Unverified

## Overview

Samba is an open-source implementation of the SMB/CIFS protocol, used for file and printer sharing across networks, commonly in offensive security to host malicious files accessible via smb:// for protocol-based exploits.

## Description

Samba enables cross-platform file sharing, allowing attackers to expose payloads like executable .desktop files publicly without authentication. In this context, it's configured for a guest-accessible 'public' share to deliver RCE vectors in desktop apps like Rocket.Chat that mishandle external protocols. Features include configurable shares, permission controls, and integration with Linux filesystems.

## Features

- Feature 1: Cross-platform SMB server emulation for Windows-compatible shares
- Feature 2: Guest access and anonymous browsing for easy payload delivery
- Feature 3: Executable file support over network, enabling direct launches

## Installation

### Requirements

- Linux distribution with apt/yum (e.g., Ubuntu)
- Root access for configuration

### Install Commands

```bash
sudo apt update
sudo apt install samba
```

## Basic Usage

```bash
smbd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-D` | Run as daemon |
| `--configfile` | Specify smb.conf path |
| `-V` | Show version |

## Examples

### Example 1: Basic Usage

Start Samba server:

```bash
sudo systemctl start smbd
```

### Example 2: Advanced Usage

Test share access:

```bash
smbclient //attacker.tld/public -U%
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Standard Application Layer Protocol]] Application Layer Protocol: Web Protocols (adapted for SMB)

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on TCP/445 with anonymous SMB sessions
- Log entries for guest share access in /var/log/samba/
- Anomalous executable files in shares monitored by file integrity tools

## Related Procedures


## Related Tools

- [[Related Tool: Impacket]]
- [[Related Tool: Metasploit SMB Modules]]

## References

- Official documentation: https://www.samba.org/samba/docs/
- Related resources: SMB protocol specs
