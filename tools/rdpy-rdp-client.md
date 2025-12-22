---
id: 2702a266-913e-4dc6-8f76-a9cfa5b9e420
type: tool
verified: true
created_at: '2019-08-28T21:17:17.788983+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - rdp
  - remote-access
  - lateral-movement
  - python
url: 'https://github.com/citronneur/rdpy'
validated: true
---

# rdpy-rdp-client

**Status**: Unverified

## Overview

RDPY is a pure Python implementation of the Microsoft Remote Desktop Protocol (RDP), providing both client and server functionality. Built on the Twisted event-driven networking engine, it's ideal for security testing, automation of RDP interactions, and protocol analysis in red team operations, such as lateral movement across Windows networks.

## Description

RDPY enables the creation of RDP clients and servers without relying on native Windows tools. It supports standard RDP security (basic encryption), RDP over SSL (using TLS), and Network Level Authentication (NLA) via NTLMv2. This makes it valuable for scripting RDP connections, testing credentials, or simulating RDP servers in controlled environments. In offensive security, it's used for remote access post-exploitation or evading detection by avoiding common RDP clients like mstsc.exe.

## Features

- Feature 1: Pure Python RDP client and server implementation, cross-platform compatibility without native dependencies.
- Feature 2: Support for RDP security layers including basic, TLS (SSL), and NLA with NTLMv2 authentication.
- Feature 3: Event-driven architecture via Twisted, allowing integration into larger automation scripts for batch RDP testing.
- Feature 4: Protocol-level access for custom modifications, useful for fuzzing or custom payload injection.

## Installation

### Requirements

- Python 2.7 or 3.x (Twisted library required: pip install twisted)
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/citronneur/rdpy.git
cd rdpy

# Install dependencies
pip install twisted

# Install RDPY
python setup.py install
```

For Kali Linux/Ubuntu:

```bash
sudo apt update
sudo apt install python3-pip git
pip3 install twisted
# Then clone and install as above
```

## Basic Usage

```python
python -m rdpy.rdesktop --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -u, --user | Specify username for authentication |
| -p, --password | Specify password for authentication |
| --security | Set security protocol (rdp, tls, nla) |
| --width, --height | Set remote desktop resolution |

## Examples

### Example 1: Basic Usage

Connect to an RDP server with basic credentials:

```python
python -m rdpy.rdesktop 192.168.1.100 -u administrator -p P@ssw0rd
```

### Example 2: Advanced Usage

Connect with NLA and custom resolution:

```python
python -m rdpy.rdesktop 192.168.1.100 -u user -p pass --security=nla --width=1280 --height=720
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote Desktop Protocol]] Remote Desktop Protocol
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Python processes spawning RDP connections (e.g., via Sysmon Event ID 1 with Image: python.exe and CommandLine containing rdpy.rdesktop).
- Detection method 2: Network traffic analysis for RDP protocol (TCP 3389) originating from non-standard clients or unusual user agents.
- Detection method 3: Log NTLM authentication attempts from Python-based clients in Windows Event Logs (Event ID 4624 with Logon Type 3).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/xfreerdp]]
- [[tools/remmina]]

## References

- Official GitHub Repository: https://github.com/citronneur/rdpy
- Twisted Documentation: https://twistedmatrix.com/
- RDP Protocol Specification: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/
