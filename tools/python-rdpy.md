---
id: 9b60201d-a518-4656-817f-0329e5d4fdd4
type: tool
verified: true
created_at: '2019-08-28T21:17:30.898157+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - rdp
  - remote-desktop
  - python
  - lateral-movement
  - protocol-implementation
url: 'https://github.com/citronneur/rdpy'
validated: true
---

# python-rdpy

**Status**: Unverified

## Overview

RDPY is a pure Python implementation of the Microsoft Remote Desktop Protocol (RDP), supporting both client and server sides. Built on the Twisted event-driven networking engine, it is useful for security testing, protocol analysis, and simulating RDP connections in red team operations or defensive research.

## Description

RDPY enables the creation of RDP clients and servers without relying on native Windows components, making it ideal for cross-platform environments. It supports standard RDP security layers, RDP over SSL (using TLS), and Network Level Authentication (NLA) via NTLMv2. Common use cases include testing RDP vulnerabilities, replaying RDP sessions, or implementing custom RDP proxies for man-in-the-middle attacks in controlled settings.

## Features

- **Pure Python Implementation**: No external dependencies beyond Python libraries; runs on any platform with Python.
- **Client and Server Support**: Full RDP client for connecting to servers and server mode for accepting connections.
- **Security Protocols**: Implements basic RDP security, CredSSP for NLA, and TLS for encrypted sessions.
- **Event-Driven Architecture**: Leverages Twisted for handling asynchronous network I/O, suitable for high-performance scenarios.
- **Extensibility**: Modular design allows customization for specific protocol behaviors or integrations.

## Installation

### Requirements

- Python 2.7 or 3.x (tested on 3.6+ recommended)
- Twisted library (pip install twisted)
- Optional: cryptography for enhanced SSL support

### Install Commands

```bash
# Clone the repository
git clone https://github.com/citronneur/rdpy.git
cd rdpy

# Install dependencies
pip install -r requirements.txt

# Install RDPY
python setup.py install
```

For Kali Linux/Ubuntu:

```bash
sudo apt update
sudo apt install python3-pip git
# Then follow the clone and install steps above
```

## Basic Usage

```python
python -m rdpy --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --version | Display RDPY version |
| --security | Specify security layer (standard, tls, nla) |

## Examples

### Example 1: Basic Usage (Start RDP Client)

Use the client module to connect to an RDP server:

```python
python -m rdpy.client 192.168.1.100 -u username -p password
```

### Example 2: Advanced Usage (Start RDP Server with TLS)

Launch a server with SSL support:

```python
python -m rdpy.server -p 3389 --certificate server.crt --private-key server.key
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote Desktop Protocol]] Remote Desktop Protocol
- [[Remote Desktop Protocol]] Account Use Policy

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on TCP port 3389 with Python/Twisted signatures in packet captures.
- Process monitoring for python.exe or rdpy modules spawning network connections.
- Log analysis for unusual RDP authentication attempts (e.g., NTLMv2 patterns from non-Windows sources).
- Behavioral detection of Python scripts establishing RDP sessions in unexpected contexts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Twisted]]
- [[tools/Impacket]] (for complementary NTLM handling)

## References

- Official GitHub Repository: https://github.com/citronneur/rdpy
- RDP Protocol Documentation: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdp/
- Twisted Documentation: https://twistedmatrix.com/documents/current/core/howto/
