---
id: a458554e-06f7-4c19-9b0c-886192ea36bd
type: tool
verified: true
created_at: '2019-08-28T21:17:29.257551+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
description: >-
  TrevorC2 is a command and control (C2) framework that uses HTTP/HTTPS
  communications disguised as legitimate website traffic to tunnel client-server
  interactions for covert command execution.
url: 'https://github.com/trustedsec/TrevorC2'
tags:
  - c2
  - command-and-control
  - evasion
  - post-exploitation
platforms:
  - Linux
  - Windows
commands:
  - '[[commands/trevorc2-start-server]]'
  - '[[commands/trevorc2-generate-stager]]'
  - '[[commands/trevorc2-list-team-servers]]'
validated: true
---

# TrevorC2

**Status**: Unverified

## Overview

TrevorC2 is an advanced command and control framework designed for red team operations and penetration testing. It enables operators to establish persistent communication channels with compromised hosts by tunneling commands over HTTP/HTTPS traffic that mimics legitimate web browsing. This allows for covert execution of commands on target systems while evading detection from network security tools that monitor for anomalous C2 patterns.

Common use cases include post-exploitation activities such as lateral movement, data exfiltration, and maintaining persistence in environments where traditional C2 protocols might be blocked.

## Description

TrevorC2 operates by hosting a legitimate-looking website on the attacker's server, which serves as the communication endpoint. Agents (stagers) deployed on target machines poll this site for commands, executing them and posting results back through the same channel. The framework supports multiple team servers for scalability, customizable HTTP headers and payloads to blend with normal traffic, and various agent types for different operating systems. It is particularly useful in scenarios requiring low-and-slow operations to avoid behavioral detection.

## Features

- **HTTP/HTTPS Tunneling**: Disguises C2 traffic as regular web requests to a browsable site.
- **Multi-Platform Agents**: Supports Windows, Linux, and macOS implants.
- **Team Server Support**: Allows multiple operators to manage agents via shared servers.
- **Customizable Evasion**: Configurable delays, user-agents, and jitter to mimic human browsing.
- **Payload Generation**: Built-in tools for creating stagers in various formats (EXE, DLL, PowerShell scripts).
- **Listener Management**: Handles multiple listeners with domain fronting capabilities.

## Installation

### Requirements

- Python 3.6+
- Git
- A domain or IP for hosting the C2 server (HTTPS recommended for production)
- Web server capabilities (e.g., Apache or Nginx for the fake site)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/trustedsec/TrevorC2.git /opt/TrevorC2
cd /opt/TrevorC2

# Install Python dependencies
pip3 install -r requirements.txt

# Set up the database (SQLite by default)
python3 trevorc2.py --help  # Verify installation
```

For production, configure a reverse proxy (e.g., Nginx) to serve the browsable site at the root path while proxying API calls to the TrevorC2 backend.

## Basic Usage

```bash
trevorc2.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-H, --host` | IP address to bind the server to (default: 0.0.0.0) |
| `-P, --port` | Port for the HTTP listener (default: 80) |
| `-u, --url` | Base URL for the team server |
| `-t, --teamserver` | Name of the team server to connect to |
| `-v, --verbose` | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Start a simple team server:

```bash
python3 trevorc2.py -H 0.0.0.0 -P 80 -u http://yourdomain.com
```

### Example 2: Advanced Usage

Generate a Windows stager and list connected agents:

```bash
# Generate stager
python3 trevorc2.py -u windows -t MyTeamServer

# In another terminal, start server and monitor
python3 trevorc2.py -H 0.0.0.0 -P 443 --https
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol
- [[Protocol Tunneling]] Protocol Tunneling
- [[Connection Proxy]] Proxy

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP POST requests to legitimate-looking domains with encoded payloads.
- High volume of polling requests from internal hosts to external IPs.
- Anomalous user-agents or headers inconsistent with browser traffic.
- Database files (SQLite) with agent check-ins on compromised servers.
- Network flows showing bidirectional HTTP traffic without corresponding browser activity.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cobalt Strike]]
- [[tools/Empire]]
- [[Sliver]]

## References

- Official GitHub: https://github.com/trustedsec/TrevorC2
- TrustedSec Documentation: https://trustedsec.com/resources/tools/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1071/
