---
id: aff6b2f1-76fe-43fe-adaa-8054fc173d7f
name: rdpy-rdpmitm
type: tool
verified: true
created_at: '2019-08-28T21:17:25.947300+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - rdp
  - mitm
  - lateral-movement
  - credential-access
  - python
url: 'https://github.com/citronneur/rdpy'
validated: true
---

# rdpy-rdpmitm

**Status**: Unverified

## Overview

rdpy-rdpmitm is a component of the RDPY library, a pure Python implementation of the Microsoft Remote Desktop Protocol (RDP) for both client and server sides. It enables man-in-the-middle (MITM) attacks on RDP connections, allowing interception, logging, and potential modification of RDP traffic. Commonly used in red team operations for credential capture, session hijacking, or traffic analysis in lateral movement scenarios.

## Description

Built on the Twisted event-driven networking engine, RDPY supports standard RDP security layers, RDP over SSL (RD Gateway), and Network Level Authentication (NLA) via NTLMv2. The rdpmitm tool specifically acts as a proxy between RDP clients and servers, facilitating attacks like credential harvesting from authentication exchanges or injecting payloads into sessions. It is lightweight and requires no additional dependencies beyond Python and Twisted, making it suitable for offensive security testing in Windows environments.

## Features

- **MITM Proxying**: Intercept and forward RDP connections transparently.
- **Protocol Support**: Handles RDP, SSL-encrypted RDP, and NLA authentication.
- **Logging Capabilities**: Capture credentials, keystrokes, and session data.
- **Event-Driven**: Scalable for multiple concurrent sessions using Twisted.
- **Pure Python**: No compilation needed; runs on any Python-supported platform.

## Installation

### Requirements

- Python 2.7 or 3.x
- Twisted library (pip install twisted)
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/citronneur/rdpy.git
cd rdpy

# Install dependencies
pip install -r requirements.txt

# Install RDPY
python setup.py install

# Alternative: Direct pip install (if available)
pip install rdpy
```

For Kali Linux/Ubuntu:

```bash
sudo apt update
sudo apt install python3-pip git
# Then follow the clone and install steps above
```

## Basic Usage

```python
python -m rdpy.rdpmitm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -l, --listen | Local address:port to listen on |
| -r, --remote | Remote RDP server address:port |
| --ssl | Enable SSL support |
| --log-level | Set logging verbosity (debug, info, etc.) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Set up a basic MITM proxy listening on port 13389 and forwarding to the target RDP server.

```python
python -m rdpy.rdpmitm -l 0.0.0.0:13389 -r 192.168.1.100:3389
```

Direct clients to connect to the attacker's IP on port 13389 instead of the real server.

### Example 2: Advanced Usage

Intercept with SSL and increased logging.

```python
python -m rdpy.rdpmitm -l 127.0.0.1:13389 -r 192.168.1.100:3389 --ssl --log-level debug
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and Relay (for RDP relay aspects)
- [[Remote Desktop Protocol]] Remote Services: Remote Desktop Protocol
- [[Password Filter DLL]] Modify Authentication Process: Password Filter DLL (for credential interception)

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual RDP connections to non-standard ports (e.g., 13389 instead of 3389).
- Network traffic showing RDP handshakes proxied through unexpected IPs.
- Python processes with Twisted event loops and RDP protocol signatures in logs.
- Increased NTLM authentication attempts or anomalous SSL handshakes on RDP ports.
- Monitor for python.exe or rdpy modules in process trees during RDP sessions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rdpwrap]]
- [[tools/bettercap]]

## References

- Official GitHub: https://github.com/citronneur/rdpy
- RDPY Documentation: Included in repo README
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1021/001/
