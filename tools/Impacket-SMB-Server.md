---
type: tool
verified: true
platforms:
  - Linux
  - Windows
tags:
  - smb
  - server
url: 'https://github.com/SecureAuthCorp/impacket'
category: Post-Exploitation
validated: true
---

# Impacket-SMB-Server

**Status**: ✓ Verified

## Overview

Impacket-SMB-Server is a Python-based SMB server implementation from the Impacket suite, designed for hosting files over the SMB protocol. It is commonly used in penetration testing to serve payloads, share files, or facilitate lateral movement by allowing remote systems to access hosted content via SMB shares. For compatibility with modern Windows systems (Windows 7+), the -smb2support option is recommended to enable SMBv2 protocol support.

## Description

The tool creates a temporary SMB server that exposes a specified directory as a network share. It supports basic SMB operations like file listing, reading, and writing, making it ideal for transferring tools or executables to compromised hosts without relying on HTTP or other protocols. Impacket's implementation is lightweight and does not require administrative privileges on the host running the server, but firewall rules may need adjustment to allow inbound SMB traffic on ports 139/445.

## Features

- Simple SMB share hosting with configurable share name and path
- Support for SMBv1 and SMBv2 (via -smb2support flag)
- Configurable IP binding and username/password authentication
- Callback mechanisms for protocol negotiation (e.g., UUID handling for Windows clients)
- Integration with other Impacket tools for authentication and protocol manipulation

## Installation

### Requirements

- Python 3.6+
- Impacket library (provides smbserver.py script)

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install impacket-scripts

# Manual installation via pip (Linux/Windows)
pip install impacket

# For Windows, ensure Python is in PATH and run as administrator if needed
pip install impacket
```

After installation, the smbserver.py script is available in the Impacket bin directory or via direct invocation if added to PATH.

## Basic Usage

```bash
smbserver.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-smb2support` | Enable SMBv2 protocol support for modern clients |
| `-ip IP` | Bind to specific IP address (default: all interfaces) |
| `-user USERNAME` | Set username for share authentication |
| `-password PASSWORD` | Set password for share authentication |
| `-comment COMMENT` | Add a description to the share |

## Examples

### Example 1: Basic Usage

Launch a simple SMB server sharing the /tmp directory as 'share'.

```bash
smbserver.py share /tmp
```

### Example 2: Advanced Usage

Launch with SMBv2 support, authentication, and bound to a specific IP.

```bash
smbserver.py share /tmp -smb2support -ip 192.168.1.100 -user attacker -password secret
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]] Exfiltration Over Unencrypted Non-C (for file transfer via SMB)
- [[Remote File Copy]] Ingress Tool Transfer (hosting payloads for download)
- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares (facilitating lateral movement)

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on TCP ports 139/445 with SMB protocol signatures (e.g., via Wireshark or Zeek)
- Log entries for SMB server startups in process monitoring (e.g., Python processes spawning smbserver.py)
- Unusual inbound SMB connections from attacker-controlled IPs
- File access logs on shares showing anomalous downloads (e.g., payloads or tools)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Impacket-Suite]]
- [[tools/Responder]]

## References

- Official GitHub: https://github.com/SecureAuthCorp/impacket
- Impacket Documentation: https://www.secureauth.com/labs/impacket
- SMB Protocol Overview: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2
