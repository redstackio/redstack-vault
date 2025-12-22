---
id: 043c16dc-4177-40bb-a9bf-5efaf88b1232
name: rdpy-rdphoneypot
type: tool
verified: true
created_at: '2019-08-28T21:17:31.818103+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - honeypot
  - rdp
  - python
  - network
url: 'https://github.com/citronneur/rdpy'
validated: true
---

# rdpy-rdphoneypot

**Status**: Unverified

## Overview

rdpy-rdphoneypot is a component of the RDPY library, providing a pure Python implementation of an RDP (Remote Desktop Protocol) honeypot server. It simulates an RDP service to attract and log attacker interactions, supporting standard RDP security, SSL/TLS encryption, and NLA (Network Level Authentication) via NTLMv2. Commonly used in defensive security to monitor RDP brute-force attempts, reconnaissance, or exploitation efforts.

## Description

Built on the Twisted event-driven networking engine, rdpy-rdphoneypot emulates a legitimate RDP server without requiring Windows or RDP-specific binaries. It captures connection details, authentication attempts, and protocol handshakes, making it ideal for threat intelligence gathering, red team deception, or blue team monitoring in environments where RDP exposure is a risk. The tool does not execute real remote desktop sessions but logs all interactions for analysis.

## Features

- **Protocol Emulation**: Full support for RDP client-server negotiation, including bitmap handling and clipboard redirection simulation.
- **Security Layers**: Implements standard RDP security (RC4 encryption), CredSSP for SSL/TLS, and NLA with NTLMv2 authentication.
- **Logging and Analysis**: Detailed logging of connection attempts, credentials tried, and protocol messages.
- **Customizable**: Options for host/port binding, SSL certificates, and log levels.
- **Lightweight**: Pure Python, no external dependencies beyond Twisted and cryptography libraries.

## Installation

### Requirements

- Python 3.6+ (with pip)
- Twisted library (automatically installed via pip)
- Optional: OpenSSL for generating SSL certificates

### Install Commands

```bash
# Install via pip (includes full RDPY library)
pip install rdpy

# For development, clone from GitHub
git clone https://github.com/citronneur/rdpy.git
cd rdpy
pip install -e .
```

On Kali Linux/Ubuntu:

```bash
sudo apt update
sudo apt install python3-pip python3-dev
pip3 install rdpy
```

For SSL support, generate self-signed certs:

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
```

## Basic Usage

```bash
rdpy-rdphoneypot --help
```

This displays available options like --host, --port, --ssl, --log-level.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --host $_HOST | Bind to specific IP (default: 0.0.0.0) |
| -p, --port $_PORT | Listen on custom port (default: 3389) |
| --ssl | Enable SSL/TLS support |
| --cert $_CERT | Path to SSL certificate |
| --key $_KEY | Path to private key |
| --log-level $_LEVEL | Set logging verbosity (debug, info, etc.) |

## Examples

### Example 1: Basic Usage

Start the honeypot on default settings:

```bash
[[commands/rdpy-rdphoneypot-start-basic]]
```

### Example 2: Advanced Usage

Start with debug logging and SSL:

```bash
[[commands/rdpy-rdphoneypot-start-with-ssl]] --log-level debug --cert server.crt --key server.key
```

### Example 3: Custom Host and Port

```bash
rdpy-rdphoneypot --host 192.168.1.10 --port 3390 --log-level info
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Remote Management]] Windows Remote Desktop Protocol (for emulation and detection)
- [[Valid Accounts]] Valid Accounts (to log credential attempts)

### Tactics

- [[Impact]] Impact (deception via honeypot)
- [[Defense Evasion]] Defense Evasion (simulating services to mislead attackers)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring: Look for python processes running rdpy-rdphoneypot or Twisted servers on port 3389.
- Network logs: Inbound connections to non-standard RDP ports or unusual SSL handshakes on RDP.
- File system: Presence of rdpy library in Python site-packages or custom SSL certs.
- Log analysis: Honeypot logs in /tmp or user directories showing captured RDP attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Twisted]] (underlying networking engine)
- [[tools/Cowrie]] (similar SSH honeypot for comparison)
- [[tools/Honeytrap]] (general-purpose honeypot)

## References

- Official GitHub: https://github.com/citronneur/rdpy
- RDPY Documentation: Included in the repository README
- Related: Microsoft RDP Protocol Specs (for deeper protocol understanding)
